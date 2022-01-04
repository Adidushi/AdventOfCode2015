from dataclasses import dataclass
from typing import Iterator, Tuple
from math import prod


@dataclass
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int

    def capacity(self, amount) -> int:
        return amount * self.capacity

    def durability(self, amount) -> int:
        return amount * self.durability

    def flavor(self, amount) -> int:
        return amount * self.flavor

    def texture(self, amount) -> int:
        return amount * self.texture

    def calories(self, amount) -> int:
        return amount * self.calories


def parse_line(line: str) -> Ingredient:
    name, line = line.split(': ')
    capacity, durability, flavor, texture, calories = [
        int(thing.split()[1]) for thing in line.split(',')]
    return Ingredient(name, capacity, durability, flavor, texture, calories)


def generate_amounts(total_sum: int, ingredients=None):
    for i in range(1, total_sum):
        for j in range(1, total_sum-i):
            for k in range(1, total_sum-i-j):
                if ingredients:
                    if sum_property((i, j, k, total_sum-i-j-k), Ingredient.calories, ingredients) == 500:
                        yield(i, j, k, total_sum-i-j-k)
                else:
                    yield(i, j, k, total_sum-i-j-k)


def sum_property(amounts, func, ingredients):
    score = 0
    for index, ingredient in enumerate(ingredients):
        score += func(ingredient, amounts[index])
    return score if score > 0 else 0


def calculate(amounts: Tuple[int, int, int, int], ingredients: list[Ingredient]) -> int:
    total_score = 1

    for property in (Ingredient.capacity, Ingredient.durability, Ingredient.flavor, Ingredient.texture):
        total_score *= sum_property(amounts, property, ingredients)
    return total_score


def q1():
    with open('day 15\input.txt', 'r') as f:
        input = f.read().splitlines()

    ingredients = [parse_line(line) for line in input]

    return max(calculate(amounts, ingredients) for amounts in generate_amounts(100))


def q2():
    with open('day 15\input.txt', 'r') as f:
        input = f.read().splitlines()

    ingredients = [parse_line(line) for line in input]

    return max(calculate(amounts, ingredients) for amounts in generate_amounts(100, ingredients))


if __name__ == '__main__':
    from time import perf_counter as pc
    st = pc()
    print(f'Part 1: {q1()}')
    pt1 = pc()
    print(f'Part 2: {q2()}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 1: {(pt1-st)*1000}ms\n\
            Part 2: {(pt2-pt1)*1000}ms\n\
            Total: {(pt2-st)*1000}ms')
