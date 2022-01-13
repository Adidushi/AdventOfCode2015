from dataclasses import dataclass
from itertools import combinations


@dataclass
class Item:
    armor: int
    damage: int
    cost: int


@dataclass
class Character:
    hp: int
    damage: int
    armor: int

    def hurt(self, damage):
        self.hp -= max(1, damage - self.armor)


weapons = [Item(0, 4, 8),
           Item(0, 5, 10),
           Item(0, 6, 25),
           Item(0, 7, 40),
           Item(0, 8, 74)]

armor = [Item(1, 0, 13),
         Item(2, 0, 31),
         Item(3, 0, 53),
         Item(4, 0, 75),
         Item(5, 0, 102),
         Item(0, 0, 0)]

rings = [Item(1, 0, 20),
         Item(2, 0, 40),
         Item(3, 0, 80),
         Item(0, 1, 25),
         Item(0, 2, 50),
         Item(0, 3, 100),
         Item(0, 0, 0),
         Item(0, 0, 0)]


def generate_combinations():
    for weapon in weapons:
        for set in armor:
            for ring1, ring2 in combinations(rings, 2):
                yield (weapon.damage + ring1.damage + ring2.damage, set.armor + ring1.armor + ring2.armor, weapon.cost + set.cost + ring1.cost + ring2.cost)


def battle(character: Character, boss: Character):
    while character.hp > 0 and boss.hp > 0:
        boss.hurt(character.damage)
        if boss.hp <= 0:
            return True
        character.hurt(boss.damage)
    return False


def q1(boss_hp, boss_damage, boss_armor):
    successes = set()

    for damage, armor, cost in generate_combinations():

        character = Character(100, damage, armor)
        boss = Character(boss_hp, boss_damage, boss_armor)
        if battle(character, boss):
            successes.add(cost)

    return min(successes)


def q2(boss_hp, boss_damage, boss_armor):
    fails = set()

    for damage, armor, cost in generate_combinations():

        character = Character(100, damage, armor)
        boss = Character(boss_hp, boss_damage, boss_armor)
        if not battle(character, boss):
            fails.add(cost)

    return max(fails)


if __name__ == '__main__':
    from time import perf_counter as pc
    st = pc()
    print(f'Part 1: {q1(109, 8, 2)}')
    pt1 = pc()
    print(f'Part 2: {q2(109, 8, 2)}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 1: {(pt1-st)*1000}ms\n\
            Part 2: {(pt2-pt1)*1000}ms\n\
            Total: {(pt2-st)*1000}ms')
