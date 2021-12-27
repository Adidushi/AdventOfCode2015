from copy import deepcopy


def parse(input: list[str]):
    all_nodes = set()
    weights = dict()
    for line in input:
        origin, _, destination, _, cost = line.split()
        cost = int(cost)
        weights[(origin, destination)] = cost
        weights[(destination, origin)] = cost
        all_nodes.add(origin)
        all_nodes.add(destination)

    return weights, all_nodes


def visit_neighbors(current_node, current_sum, paths, unvisited, func):
    unvisited = deepcopy(unvisited)
    unvisited.remove(current_node)
    if not unvisited:
        return current_sum

    return func(visit_neighbors(next_node, current_sum + paths[(current_node, next_node)], paths, unvisited, func) for next_node in unvisited)


def q1():
    with open('day 09\input.txt', 'r') as f:
        input = f.read().splitlines()

    weights, all_nodes = parse(input)

    return min(visit_neighbors(node, 0, weights, deepcopy(all_nodes), min) for node in all_nodes)


def q2():
    with open('day 09\input.txt', 'r') as f:
        input = f.read().splitlines()

    weights, all_nodes = parse(input)

    return max(visit_neighbors(node, 0, weights, deepcopy(all_nodes), max) for node in all_nodes)


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
