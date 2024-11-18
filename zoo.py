class Enclosure:
    def __init__(self, name):
        self.name = name
        self.is_clean = False
        self.is_open = False
        self.animals = []

    def open_enclosure(self):
        print(f"{self.name} is now open")
        self.is_open = True

    def close_enclosure(self):
        print(f"{self.name} is now closed.")
        self.is_open = False

    def add_animals(self, animals):
        for animal in animals:
            print(f"{animal.kind} {animal.name} added to {self.name}")
            self.animals.append(animal)


class Animals:
    def __init__(self, kind, name):
        self.kind = kind
        self.name = name
        self.is_hungry = True
        self.is_happy = False

    def check_happiness(self, enclosure: Enclosure):
        if enclosure.is_clean and not self.is_hungry:
            self.is_happy = True
        else:
            self.is_happy = False
        print(f"{self.name} is happy {self.is_happy}")

class Zookeeper:
    def __init__(self, name):
        self.name = name

    def clean_enclosure(self, enclosure: Enclosure):
        print(f"{self.name} cleaned the {enclosure.name}")
        enclosure.is_clean = True

    def feed_animal(self, animal: Animals):
        print(f"{self.name} fed the {animal.name}")
        animal.is_hungry = False

class Lion(Animals):
    def __init__(self, name):
        super().__init__('Lion', name)
        self.name = name

class Monkey(Animals):
    def __init__(self, name):
        super().__init__('Monkey', name)
        self.name = name

class Giraffe(Animals):
    def __init__(self, name):
        super().__init__('Giraffe', name)
        self.name = name


def zoo_day():
    zookeeper_Bob = Zookeeper("Bob")
    zookeeper_Alis = Zookeeper("Alis")

    lion_enclosure = Enclosure("Lion enclosure")
    monkey_enclosure = Enclosure("Monkey enclosure")
    giraffe_enclosure = Enclosure("Giraffe enclosure")

    Jon = Lion("Jon")
    Bella = Lion("Bella")
    Lu = Monkey("Lu")
    Max = Monkey("Max")
    Luna = Giraffe("Luna")
    Spot = Giraffe("Spot")

    lion_enclosure.open_enclosure()
    lion_enclosure.add_animals([Jon, Bella])
    lion_enclosure.close_enclosure()

    monkey_enclosure.open_enclosure()
    monkey_enclosure.add_animals([Lu, Max])
    monkey_enclosure.close_enclosure()

    giraffe_enclosure.open_enclosure()
    giraffe_enclosure.add_animals([Luna, Spot])
    giraffe_enclosure.close_enclosure()

    zookeeper_Bob.clean_enclosure(lion_enclosure)
    zookeeper_Bob.feed_animal(Jon)
    zookeeper_Bob.feed_animal(Bella)

    zookeeper_Alis.clean_enclosure(monkey_enclosure)
    zookeeper_Alis.feed_animal(Lu)
    zookeeper_Alis.feed_animal(Max)

    zookeeper_Alis.clean_enclosure(giraffe_enclosure)
    zookeeper_Alis.feed_animal(Luna)
    zookeeper_Alis.feed_animal(Spot)

    Jon.check_happiness(lion_enclosure)
    Bella.check_happiness(lion_enclosure)
    Lu.check_happiness(monkey_enclosure)
    Max.check_happiness(monkey_enclosure)
    Luna.check_happiness(giraffe_enclosure)
    Spot.check_happiness(giraffe_enclosure)

if __name__ == '__main__':
    zoo_day()
