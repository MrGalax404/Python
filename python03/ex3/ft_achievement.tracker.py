#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_achievement.tracker.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: shkrasni <shkrasni@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/25 12:11:44 by shkrasni            #+#    #+#            #
#   Updated: 2026/11/25 14:32:54 by shkrasni           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random


def get_all_achievements() -> set[str]:
    return {
        'Crafting Genius', 'Strategist', 'World Savior',
        'Speed Runner', 'Survivor', 'Master Explorer',
        'Treasure Hunter', 'Unstoppable', 'First Steps',
        'Collector Supreme', 'Untouchable', 'Sharp Mind',
        'Boss Slayer',
    }


def gen_player_achievements() -> set[str]:
    all_achievements: set[str] = get_all_achievements()
    count: int = random.randint(2, len(all_achievements))
    selected: set[str] = set(random.sample(list(all_achievements), count))
    return selected


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()

    p_alice: set[str] = gen_player_achievements()
    p_bob: set[str] = gen_player_achievements()
    p_charlie: set[str] = gen_player_achievements()
    p_dylan: set[str] = gen_player_achievements()

    print(f"Player Alice: {p_alice}")
    print(f"Player Bob: {p_bob}")
    print(f"Player Charlie: {p_charlie}")
    print(f"Player Dylan: {p_dylan}")
    print()

    print(f"All distinct achievements: {get_all_achievements()}")
    print()

    common: set[str] = set.intersection(p_alice, p_bob, p_charlie, p_dylan)
    print(f"Common achivements: {common}")
    print()

    only_alice: set[str] = set.difference(p_alice, p_bob, p_charlie, p_dylan)
    only_bob: set[str] = set.difference(p_bob, p_alice, p_charlie, p_dylan)
    only_charlie: set[str] = set.difference(p_charlie, p_alice, p_bob, p_dylan)
    only_dylan: set[str] = set.difference(p_dylan, p_alice, p_bob, p_charlie)

    print(f"Only Alice has: {only_alice}")
    print(f"Only Bob has: {only_bob}")
    print(f"Only Charlie has: {only_charlie}")
    print(f"Only Dylan has: {only_dylan}")
    print()

    missing_alice: set[str] = set.difference(get_all_achievements(), p_alice)
    missing_bob: set[str] = set.difference(get_all_achievements(), p_bob)
    missing_chrl: set[str] = set.difference(get_all_achievements(), p_charlie)
    missing_dylan: set[str] = set.difference(get_all_achievements(), p_dylan)

    print(f"Alice is missing: {missing_alice}")
    print(f"Bob is missing: {missing_bob}")
    print(f"Charlie is missing: {missing_chrl}")
    print(f"Dylan is missing: {missing_dylan}")


if __name__ == "__main__":
    main()
