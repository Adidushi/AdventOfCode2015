from itertools import permutations


def parse_line(line: str) -> tuple:
    # Alice would gain 54 happiness units by sitting next to Bob.
    p1, _, sign, amount, _, _, _, _, _, _, p2 = line.split()
    if sign == 'gain':
        amount = int(amount)
    else:
        amount = -1 * int(amount)

    return ((p1, p2), amount)


def calculate_happiness(order: list, values: dict) -> int:
    total_happiness = 0
    # print(f'order: {order}', end='')
    order = order[:]
    order.append(order[0])

    for person_1, person_2 in zip(order, order[1:]):
        total_happiness += values[person_1, person_2]
        total_happiness += values[person_2, person_1]
    # print(f', total happiness: {total_happiness}')

    return total_happiness


def q1():
    with open('day 13\input.txt', 'r') as f:
        input = f.read().splitlines()

    values = dict()
    for line in input:
        people, happiness = parse_line(line.replace('.', ''))
        values[people] = happiness

    all_people = set()
    for k in values.keys():
        p1, p2 = k
        all_people.add(p1)
        all_people.add(p2)

    perms = list(permutations(all_people))

    return max(calculate_happiness(list(perm), values) for perm in perms)


def q2():
    with open('day 13\sample.txt', 'r') as f:
        input = f.read().splitlines()

    values = dict()
    for line in input:
        people, happiness = parse_line(line.replace('.', ''))
        values[people] = happiness

    all_people = set()
    for k in values.keys():
        p1, p2 = k
        all_people.add(p1)
        all_people.add(p2)

    perms = list(permutations(all_people))

    return max(calculate_happiness(list(perm), values) for perm in perms)


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
