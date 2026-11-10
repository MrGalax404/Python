#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_count_harvest_recursive.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: shkrasni <shkrasni@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/05 11:02:33 by shkrasni            #+#    #+#            #
#   Updated: 2026/11/05 14:58:57 by shkrasni           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count(day):
        if (day > days):
            print("Harvest time!")
            return
        print(f"Day {day}")
        count(day + 1)
    count(1)
