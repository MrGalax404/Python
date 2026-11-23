#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_raise_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: shkrasni <shkrasni@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/23 13:20:08 by shkrasni            #+#    #+#            #
#   Updated: 2026/11/23 14:15:48 by shkrasni           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class TemperatureTooHot(Exception):
    pass


class TemperatureTooCold(Exception):
    pass


def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    temp = int(temp_str)
    if (temp > 40):
        raise TemperatureTooHot
    if (temp < 0):
        raise TemperatureTooCold
    return temp


def test_tempeature(temp_str: str) -> None:
    try:
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}°C")
    except ValueError:
        print("Caught input_temperature error: invalid literal for int() with"
              f" base 10: '{temp_str}'")
    except TemperatureTooHot:
        print(f"Caught input_temperature error: {temp_str}°C is too hot "
              "for plants (max 40°C)")
    except TemperatureTooCold:
        print(f"Caught input_temperature error: {temp_str}°C is too cold "
              "for plants (min 0°C)")


def main() -> None:
    print("=== Garden Temperature ===")
    test_tempeature("25")
    print()
    test_tempeature("abc")
    print()
    test_tempeature("100")
    print()
    test_tempeature("-50")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
