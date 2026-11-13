#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: shkrasni <shkrasni@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/11/10 15:22:35 by shkrasni            #+#    #+#            #
#   Updated: 2026/11/13 14:41:38 by shkrasni           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    class _Statistic:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def incr_grow(self) -> None:
            self._grow_count += 1

        def incr_age(self) -> None:
            self._age_count += 1

        def incr_show(self) -> None:
            self._show_count += 1

        def get_grow(self) -> int:
            return self._grow_count

        def get_age(self) -> int:
            return self._age_count

        def get_show(self) -> int:
            return self._show_count

        def display(self) -> None:
            print(f"Stats: {self._grow_count} grow, {self._age_count} age, "
                  f"{self._show_count} show")

    def __init__(self, name: str, height: float, age: int,
                 grow_rate: float = 0.8) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._grow_rate = grow_rate
        self._stats = self._Statistic()

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 2)}cm, "
              f"{self._age} days old")
        self._stats.incr_show()

    def display_stat(self) -> None:
        self._stats.display()

    def grow(self) -> None:
        self._height = self._height + self._grow_rate
        self._stats.incr_grow()

    def age(self, days: int) -> None:
        self._age = self._age + days
        self._stats.incr_age()

    @staticmethod
    def check_age(age: int) -> bool:
        if (age > 365):
            return True
        else:
            return False

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown Plant", 0.0, 0, 0)

    def set_height(self, height: float) -> None:
        if (height < 0):
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {self._height}cm")

    def set_age(self, age: int) -> bool:
        if (age < 0):
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return False
        else:
            self._age = age
            print(f"Age updated: {self._age} days")
            return True

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_stats(self) -> _Statistic:
        return self._stats


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str,
                 is_bloom: bool = False, grow_rate: float = 0.8) -> None:
        super().__init__(name, height, age, grow_rate)
        self._color = color
        self._is_bloom = is_bloom

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if (self._is_bloom):
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")

    def bloom(self) -> None:
        self._is_bloom = True


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str,
                 seed_bloom: int, is_bloom: bool = False,
                 grow_rate: float = 0.8) -> None:
        super().__init__(name, height, age, color, is_bloom, grow_rate)
        self._count_seed = 0
        self._seed_bloom = seed_bloom

    def bloom(self) -> None:
        if (self._is_bloom is False):
            self._count_seed += self._seed_bloom
            self._is_bloom = True

    def show(self) -> None:
        super().show()
        print(f" Seed: {self._count_seed}")


class Tree(Plant):
    class _TreeStatistic(Plant._Statistic):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def incr_shade(self) -> None:
            self._shade_count += 1

        def get_grow(self) -> int:
            return self._shade_count

        def display(self) -> None:
            super().display()
            print(f" {self._shade_count} shade")

    _stats: "Tree._TreeStatistic"

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float, grow_rate: float = 0.8) -> None:
        super().__init__(name, height, age, grow_rate)
        self._trunk_diameter = trunk_diameter
        self._stats = self._TreeStatistic()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self._trunk_diameter, 1)}")

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of {self._height}cm "
              f"long and {self._trunk_diameter}cm wide.")
        self._stats.incr_shade()


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, grow_rate: float = 0.8) -> None:
        super().__init__(name, height, age, grow_rate)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self._harvest_season}")
        print(f" Nutritional value: {self._nutritional_value}")

    def age(self, days: int) -> None:
        super().age(days)
        self._nutritional_value += days


def display_stat(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.display_stat()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year ? -> {Plant.check_age(30)}")
    print(f"Is 400 days more than a year ? -> {Plant.check_age(400)}")
    print()
    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red", False, 8.0)
    rose.show()
    display_stat(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_stat(rose)
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_stat(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stat(oak)
    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", 42, False, 30)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_stat(sunflower)
    print()
    print("=== Anonymous")
    anonymous = Plant.create_anonymous()
    anonymous.show()
    display_stat(anonymous)
    print("=== End of Program ===")
