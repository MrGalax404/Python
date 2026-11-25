#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_coordinate_system.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: shkrasni <shkrasni@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/23 16:06:53 by shkrasni            #+#    #+#            #
#   Updated: 2026/11/25 13:56:11 by shkrasni           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            coordinates = input("Enter new coordinates as floats "
                                "in format 'x,y,z': ")
        except KeyboardInterrupt:
            break
        try:
            x, y, z = coordinates.split(",")
        except ValueError:
            print("Invalid Synthax")
            continue
        try:
            return (float(x), float(y), float(z))
        except ValueError as e:
            print(f"Error: {e}")
    return (0, 0, 0)


def distance_to_center(x1: float, y1: float, z1: float,
                       x2: float, y2: float, z2: float,) -> float:
    distance = math.sqrt((x2 - x1) ** 2 + (y2-y1) ** 2 + (z2 - z1) ** 2)
    return distance


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    coords: tuple[float, float, float] = get_player_pos()
    if (coords is None):
        return
    print(f"Result: {coords}")
    x: float = coords[0]
    y: float = coords[1]
    z: float = coords[2]
    print(f"It includes: X={x}, Y={y}, Z={z}")
    distance: float = distance_to_center(x, y, z, 0, 0, 0)
    print(f"Distance to center: {round(distance, 4)}")
    print()
    print("Get a second set of coordinates")
    coords2: tuple[float, float, float] = get_player_pos()
    if (coords2 is None):
        return
    x2: float = coords2[0]
    y2: float = coords2[1]
    z2: float = coords2[2]
    distance2 = distance_to_center(x, y, z, x2, y2, z2)
    print(f"Distance between the 2 sets of coordinates: {round(distance2, 4)}")


if __name__ == "__main__":
    main()
