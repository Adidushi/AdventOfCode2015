from typing import List
from itertools import count, product
from copy import deepcopy


def get_neighbors(r, c, matrix):
    rows = [index for index in (r - 1, r, r + 1) if 0 <= index < len(matrix)]
    cols = [index for index in (c - 1, c, c + 1)
            if 0 <= index < len(matrix[0])]
    possible_neighbors = set(product(rows, cols))
    possible_neighbors.remove((r, c))
    for r, c in possible_neighbors:
        yield(r, c)


def count_neighbors(r, c, matrix):
    on_neighbors = 0
    for n_r, n_c in get_neighbors(r, c, matrix):
        if matrix[n_r][n_c] == '#':
            on_neighbors += 1
    return on_neighbors


def pretty(matrix):
    for line in matrix:
        print(''.join(line))

    print('=' * len(matrix[0]))


def parse(in_str: str) -> List[List[str]]:
    return [list(line.strip()) for line in in_str]


def set_corners(new_matrix):
    coords = 0, len(new_matrix)-1
    for r, c in product(coords, coords):
        new_matrix[r][c] = '#'
    return new_matrix


def do_turn(matrix, corners=False):
    new_matrix = deepcopy(matrix)
    for r, _ in enumerate(matrix):
        for c, _ in enumerate(matrix[0]):
            if matrix[r][c] == '.' and count_neighbors(r, c, matrix) == 3:
                new_matrix[r][c] = '#'
            elif matrix[r][c] == '#' and count_neighbors(r, c, matrix) == 2 or count_neighbors(r, c, matrix) == 3:
                new_matrix[r][c] = '#'
            else:
                new_matrix[r][c] = '.'
    if corners:
        new_matrix = set_corners(new_matrix)
    return new_matrix


def count_on(matrix):
    counter = 0
    for r, _ in enumerate(matrix):
        for c, _ in enumerate(matrix[0]):
            if matrix[r][c] == '#':
                counter += 1
    return counter


def q1(turns):
    with open('day 18\input.txt', 'r') as f:
        matrix = parse(f.readlines())

    for _ in range(turns):
        matrix = do_turn(matrix)

    return count_on(matrix)


def q2(turns):
    with open('day 18\input.txt', 'r') as f:
        matrix = parse(f.readlines())

    for _ in range(turns):
        matrix = do_turn(matrix, corners=True)

    return count_on(matrix)


if __name__ == '__main__':
    from time import perf_counter as pc
    st = pc()
    print(f'Part 1: {q1(100)}')
    pt1 = pc()
    print(f'Part 2: {q2(100)}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 1: {(pt1-st)*1000}ms\n\
            Part 2: {(pt2-pt1)*1000}ms\n\
            Total: {(pt2-st)*1000}ms')
