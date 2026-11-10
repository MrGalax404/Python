#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: shkrasni <shkrasni@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/10 13:22:30 by shkrasni            #+#    #+#            #
#   Updated: 2026/11/10 15:21:30 by shkrasni           ###   ########.fr      #
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

    def set_height(self, height: float) -> bool:
        if (height < 0):
            print(f"{self._name}: Error, height can't be negative")
            return False
        else:
            self._height = height
            print(f"Height updated: {self._height}cm")
            return True

    def set_age(self, age: int) -> bool:
        if (age < 0):
            print(f"{self._name}: Error, age can't be negative")
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


if __name__ == "__main__":
    print("=== Garden Security System ===")
    p1 = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    p1.show()
    print()
    if (p1.set_height(25) is False):
        print("Height update rejected")
    if (p1.set_age(30) is False):
        print("Age update rejected")
    print()
    if (p1.set_height(-10) is False):
        print("Height update rejected")
    if (p1.set_age(-10) is False):
        print("Age update rejected")
    print()
    print("Current state: ", end="")
    p1.show()
    print("=== End of Program ===")
