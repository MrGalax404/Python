#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: shkrasni <shkrasni@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/10 14:02:34 by shkrasni            #+#    #+#            #
#   Updated: 2026/11/10 15:15:11 by shkrasni           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: int,
                 grow_rate: float = 0.8) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._grow_rate = grow_rate

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")

    def grow(self) -> None:
        self._height = self._height + self._grow_rate

    def age(self) -> None:
        self._age = self._age + 1

    def set_height(self, height: float) -> None:
        if (height < 0):
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm")

    def set_age(self, age: int) -> bool:
        if (age < 0):
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return False
        else:
            self._age = age
            print(f"Age updated: {self._age} days")
            return True

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str,
                 is_bloom: bool = False, grow_rate: float = 0.8) -> None:
        super().__init__(name, height, age, grow_rate)
        self._color = color
        self._is_bloom = is_bloom

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if (self._is_bloom):
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")

    def bloom(self) -> None:
        self._is_bloom = True


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float, grow_rate: float = 0.8) -> None:
        super().__init__(name, height, age, grow_rate)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter}")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of {self._height}cm "
              f"long and {self._trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, grow_rate: float = 0.8) -> None:
        super().__init__(name, height, age, grow_rate)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def age(self) -> None:
        super().age()
        self._nutritional_value += 1


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower = Flower("Rose", 15.0, 10, "red")
    flower.show()
    print("[asking the rose to bloom]")
    flower.bloom()
    flower.show()
    print()
    print("=== Tree")
    tree = Tree("Oak", 200.0, 365, 5.0)
    tree.show()
    print("[asking the oak to produce shade]")
    tree.produce_shade()
    print()
    print("=== Vegetable")
    vegetable = Vegetable("Tomato", 5.0, 10, "April", 2.1)
    vegetable.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(1, 21):
        vegetable.age()
        vegetable.grow()
    vegetable.show()
    print("=== End of Program ===")
