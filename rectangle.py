'''
Реалізуйте клас, Rectangle врахувавши наведені нижче вимоги:

Реалізуйте конструктор для ініціалізації значень двох приватних властивостей: length та width.
напишіть метод, що повертає площу прямокутника
напишіть метод, що повертає периметр прямокутника
'''


class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def get_square(self):
        return self.__length * self.__width

    def get_perimeter(self):
        return 2 * (self.__length + self.__width)

if __name__ == '__main__':
    rectangle1 = Rectangle(length=10, width=5)
    print(f'square = {rectangle1.get_square()}')
    print(f'perimeter = {rectangle1.get_perimeter()}')