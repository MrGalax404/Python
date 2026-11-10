#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_age.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: shkrasni <shkrasni@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/05 14:55:18 by shkrasni            #+#    #+#            #
#   Updated: 2026/11/05 14:55:22 by shkrasni           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_plant_age():
    age = int(input("Enter plant age in days: "))
    if (age < 60):
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")
