#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: shkrasni <shkrasni@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/10 12:46:47 by shkrasni            #+#    #+#            #
#   Updated: 2026/11/10 13:03:48 by shkrasni           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: int,
                 grow_rate: float) -> None:
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


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    p1 = Plant("Rose", 25.0, 30, 0.8)
    p1.show()
    starting_height = p1._height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        p1.grow()
        p1.age()
        p1.show()
    total_growth = p1._height - starting_height
    print(f"Growth this week: {round(total_growth, 1)}cm")
    print("=== End of Program ===")
