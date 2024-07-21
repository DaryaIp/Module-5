class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.name = args[0]
        cls.houses_history.append(instance.name)
        return instance
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        new_floor = int(new_floor)
        if 1 <= new_floor <= self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        isinstance(other, int)
        return self.number_of_floors == other.number_of_floors
    def __add__(self, value):
        isinstance(value, int)
        self.number_of_floors += value
        return self
    def __iadd__(self, value):
        self.number_of_floors += value
        return self
    def __radd__(self, value):
        self.number_of_floors += value
        return self
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

house_1 = House('Ереван', 10)
print(House.houses_history)
house_2 = House('ЖК Горнолыжный', 15)
print(House.houses_history)
house_3 = House('ТК Европолис', 3)
print(House.houses_history)
house_4 = House('БЦ Крылатский', 18)
print(House.houses_history)
# Удаление объектов
del house_1
del house_2
print(House.houses_history)
