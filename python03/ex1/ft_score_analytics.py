#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_score_analytics.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: shkrasni <shkrasni@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/23 15:36:15 by shkrasni            #+#    #+#            #
#   Updated: 2026/11/23 16:04:48 by shkrasni           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def get_valid_scores(argv: list[str]) -> list[int]:
    scores: list[int] = [0] * len(argv)
    i: int = 0
    for arg in argv:
        try:
            scores[i] = int(arg)
            i += 1
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return scores[:i]


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    scores: list[int] = get_valid_scores(sys.argv[1:])
    argc: int = len(scores)
    if (argc == 0):
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")
    else:
        print(f"Score Processed: {scores}")
        print(f"Total players: {argc}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores)/argc}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
