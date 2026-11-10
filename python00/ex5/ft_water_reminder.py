#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_water_reminder.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: shkrasni <shkrasni@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/02 13:14:22 by shkrasni            #+#    #+#            #
#   Updated: 2026/11/05 14:59:01 by shkrasni           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_water_reminder():
    days = int(input("Days since last watering: "))
    if (days > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
