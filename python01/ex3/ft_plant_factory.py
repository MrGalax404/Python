#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_factory.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: shkrasni <shkrasni@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/10 13:08:26 by shkrasni            #+#    #+#            #
#   Updated: 2026/11/10 13:53:08 by shkrasni           ###   ########.fr      #
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
    print("=== Plant Factory Output ===")
    p1 = Plant("Rose", 25.0, 30, 0.1)
    p2 = Plant("Oak", 200.0, 365, 0.1)
    p3 = Plant("Cactus", 5.0, 90, 0.5)
    p4 = Plant("Sunflower", 80.0, 45, 0.2)
    p5 = Plant("Fern", 15.0, 120, 0.1)
    print("Created: ", end="")
    p1.show()
    print("Created: ", end="")
    p2.show()
    print("Created: ", end="")
    p3.show()
    print("Created: ", end="")
    p4.show()
    print("Created: ", end="")
    p5.show()
    print("=== End of Program ===")
