def get_size(l: int, w: int, h: int) -> int:
    return 2*(l*w + w*h + h*l) + min(l*w, w*h, h*l)


def get_length(l: int, w: int, h: int) -> int:
    return l*w*h + 2*min(l+w, l+h, w+h)


def parse(input: list) -> list:
    input = [size.split('x') for size in input]
    new = list()
    for n in input:
        new.append(int(x) for x in n)
    return new


def q1():
    with open('day 02\input.txt', 'r') as f:
        input = f.read().splitlines()
    input = parse(input)

    input = [get_size(x, y, z) for x, y, z in input]

    return sum(input)


def q2():
    with open('day 02\input.txt', 'r') as f:
        input = f.read().splitlines()
    input = parse(input)

    input = [get_length(x, y, z) for x, y, z in input]

    return sum(input)


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
