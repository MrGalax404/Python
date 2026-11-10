#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_count_harvest_iterative.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: shkrasni <shkrasni@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/02 13:41:19 by shkrasni            #+#    #+#            #
#   Updated: 2026/11/05 14:58:52 by shkrasni           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_iterative():
    my_range = range((int(input("Days until harvest: "))))
    for num in my_range:
        print(f"Day {num+1}")
    print("Harvest time!")
