#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_harvest_total.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: shkrasni <shkrasni@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/02 12:59:07 by shkrasni            #+#    #+#            #
#   Updated: 2026/11/05 14:58:47 by shkrasni           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_harvest_total():
    day1 = int(input("Day 1 harvest: "))
    day2 = int(input("Day 2 harvest: "))
    day3 = int(input("Day 3 harvest: "))
    total = day1 + day2 + day3
    print(f"Total harvest: {total}")
