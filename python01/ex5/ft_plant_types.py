#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: shkrasni <shkrasni@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/10 14:02:34 by shkrasni            #+#    #+#            #
#   Updated: 2026/11/10 14:25:01 by shkrasni           ###   ########.fr      #
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

    def set_age(self, age: int) -> None:
        if (age < 0):
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {self._age} days")

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
    print("=== End of Program ===")
