class House:
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

house_1 = House('Ереван', 10)
house_2 = House('ЖК Горнолыжный', 15)
print(house_1)
print(house_2)
print(house_1 == house_2)
house_1 = house_1 + 5
print(house_1)
print(house_1 == house_2)
house_1 += 10
print(house_1)
house_2 = 10 + house_2
print(house_2)

print(house_1 > house_2) # __gt__
print(house_1 >= house_2) # __ge__
print(house_1 < house_2) # __lt__
print(house_1 <= house_2) # __le__
print(house_1 != house_2) # __ne__