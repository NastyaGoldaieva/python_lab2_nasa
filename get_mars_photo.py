import argparse
import os.path
from datetime import datetime
import requests
import json

from PIL import Image


class NasaImage:
    def __init__(self, earth_date: str, camera: str, API_KEY: str, show_images: bool = False):
        self.earth_date = earth_date
        self.camera = camera
        self.API_KEY = API_KEY
        self.base_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
        self.out_dir = None
        self.show_images = show_images


    def __get_nasa_data(self) -> dict:
        earth_date_datatime = datetime.strptime(self.earth_date, '%Y%m%d').date()
        url_params = {
            'earth_date': earth_date_datatime,
            'camera': self.camera,
            'api_key': self.API_KEY
        }
        response = requests.get(url=self.base_url, params=url_params)
        if not response.status_code == 200:
            raise Exception(f'Failed to get response from: {response.url}\nReason: {response.reason}')
        return json.loads(response.text)

    def __create_dir(self):
        self.out_dir = f"{self.earth_date}_Curiosity_{self.camera}"
        if not os.path.exists(self.out_dir):
            os.mkdir(self.out_dir)

    def __download_images(self, nasa_data: dict):
        downloaded_images = []
        for photo in nasa_data['photos']:
            img_src = photo['img_src']
            img_name = os.path.basename(img_src)
            img_local_path = os.path.join(self.out_dir, img_name)
            img_response = requests.get(img_src)
            if img_response.status_code == 200:
                with open(img_local_path, "wb") as f:
                    f.write(img_response.content)
            else:
                raise Exception(f'Failed to download image: {img_src}')
            downloaded_images.append(img_local_path)

        print(f'Images successfully downloaded to folder: {self.out_dir}')
        return downloaded_images

    @staticmethod
    def __show_images(downloaded_images: list):
        for image in downloaded_images:
            img = Image.open(image)
            img.show(image)

    def run(self):
        nasa_data = self.__get_nasa_data()
        self.__create_dir()
        downloaded_images = self.__download_images(nasa_data)
        if self.show_images:
            self.__show_images(downloaded_images)

# python get_mars_photo.py --earth-date 20200603 --camera RHAZ --key TqacKrT3SqmhZsFojHlAAmYPRf1kmfDqGzqDal08 --show
if __name__ == '__main__':
    # for Pycharm
    # API_KEY = 'TqacKrT3SqmhZsFojHlAAmYPRf1kmfDqGzqDal08'
    # earth_date = '20200520'
    # camera = 'FHAZ'
    # show_images = True
    # nasa_image = NasaImage(earth_date, camera, API_KEY, show_images)
    # nasa_image.run()

    # for terminal
    parser = argparse.ArgumentParser(description="Download Mars photos from NASA API.")
    parser.add_argument('--earth-date', type=str, required=True, help="Earth date in format YYYYMMDD.")
    parser.add_argument('--camera', type=str, required=True, help="Camera type (e.g., FHAZ, RHAZ, etc.).")
    parser.add_argument('--key', type=str, required=True, help="NASA API key.")
    parser.add_argument('--show', action='store_true', help="Show downloaded images after downloading.")

    args = parser.parse_args()

    nasa_image = NasaImage(earth_date=args.earth_date, camera=args.camera, API_KEY=args.key, show_images=args.show)
    nasa_image.run()
