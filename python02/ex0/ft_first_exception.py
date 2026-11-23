#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_first_exception.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: shkrasni <shkrasni@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/23 13:02:08 by shkrasni            #+#    #+#            #
#   Updated: 2026/11/23 13:29:01 by shkrasni           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    return int(temp_str)


def test_tempeature(temp_str: str) -> None:
    try:
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}°C")
    except ValueError:
        print("Caught input_temperature error: invalid literal for int() with"
              f" base 10: '{temp_str}'")


def main() -> None:
    print("=== Garden Temperature ===")
    test_tempeature("25")
    print()
    test_tempeature("abc")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
