#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_seed_inventory.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: shkrasni <shkrasni@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/05 11:22:49 by shkrasni            #+#    #+#            #
#   Updated: 2026/11/05 14:59:05 by shkrasni           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_seed_inventory(seed_type: str, qty: int, unit: str) -> None:
    if (unit == "packets"):
        print(f"{seed_type.capitalize()} seeds: {qty} packets available")
    elif (unit == "grams"):
        print(f"{seed_type.capitalize()} seeds: {qty} grams total")
    elif (unit == "packets"):
        print(f"{seed_type.capitalize()} seeds: covers {qty} square meters")
    else:
        print("Unknown unit type")
