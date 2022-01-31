from functools import reduce
from itertools import combinations
from operator import mul


def q1():
    with open('day 24\input.txt', 'r') as f:
        input = [int(weight) for weight in f.read().splitlines()]
    group_weight = sum(input) // 3

    for i, val in enumerate(input):
        qes = [reduce(mul, group) for group in combinations(
            input, i) if sum(group) == group_weight]
        if qes:
            return min(qes)


def q2():
    with open('day 24\input.txt', 'r') as f:
        input = [int(weight) for weight in f.read().splitlines()]
    group_weight = sum(input) // 4

    for i, val in enumerate(input):
        qes = [reduce(mul, group) for group in combinations(
            input, i) if sum(group) == group_weight]
        if qes:
            return min(qes)


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
