#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_command_quest.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: shkrasni <shkrasni@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/23 15:11:30 by shkrasni            #+#    #+#            #
#   Updated: 2026/11/23 15:36:37 by shkrasni           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    argv: list[str] = sys.argv
    argc: int = len(argv)
    print(f"Program name: {argv[0]}")
    i: int = 1
    while (i < argc):
        print(f"Argument {i}: {argv[i]}")
        i += 1
    if (argc == 1):
        print("No arguments provided")
    print(f"Total arguments: {argc}")
