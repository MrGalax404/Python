#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_different_errors.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: shkrasni <shkrasni@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/23 13:42:15 by shkrasni            #+#    #+#            #
#   Updated: 2026/11/23 14:10:11 by shkrasni           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def garden_operations(operation_number: int) -> None:
    if (operation_number == 0):
        int("abc")
    elif (operation_number == 1):
        123 / 0
    elif (operation_number == 2):
        open("test.txt")
    elif (operation_number == 3):
        "123" + 123
    else:
        1 + 1


def test_errors(op_n: int) -> None:
    print(f"Testing operation {op_n}...")
    try:
        garden_operations(op_n)
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    except TypeError as e:
        print(e)
    else:
        print("Operation completed successfully")


def main() -> None:
    print("===  Garden Error Types Demo  ===")
    test_errors(0)
    test_errors(1)
    test_errors(2)
    test_errors(3)
    test_errors(4)
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    main()
