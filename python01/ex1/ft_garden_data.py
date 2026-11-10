#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_data.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: shkrasni <shkrasni@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/10 12:18:12 by shkrasni            #+#    #+#            #
#   Updated: 2026/11/10 12:29:24 by shkrasni           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 15, 120)
    p1.show()
    p2.show()
    p3.show()
    print("=== End of Program ===")
