from itertools import combinations


def q1(liters: int) -> int:
    with open('day 17\input.txt', 'r') as f:
        input = f.read().splitlines()
    containers = list(map(int, input))

    return sum(len(list(filter(lambda subset: sum(subset) == liters, combinations(containers, length)))) for length in range(len(containers)))


def q2(liters: int) -> int:
    with open('day 17\input.txt', 'r') as f:
        input = f.read().splitlines()
    containers = list(map(int, input))

    for length in range(len(containers)):
        num_of_subsets = len(list(filter(lambda subset: sum(
            subset) == liters, combinations(containers, length))))
        if num_of_subsets:
            return num_of_subsets


if __name__ == '__main__':
    from time import perf_counter as pc
    st = pc()
    print(f'Part 1: {q1(150)}')
    pt1 = pc()
    print(f'Part 2: {q2(150)}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 1: {(pt1-st)*1000}ms\n\
            Part 2: {(pt2-pt1)*1000}ms\n\
            Total: {(pt2-st)*1000}ms')
