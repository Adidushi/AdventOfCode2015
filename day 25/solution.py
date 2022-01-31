def get_next_number(num):
    return (num * 252533) % 33554393


def get_next_coord(coord):
    row, col = coord
    if row == 1:
        return col + 1, 1
    return row - 1, col + 1


def q1():
    index = 0
    coord = (1, 1)
    while coord != (3010, 3019):
        coord = get_next_coord(coord)
        index += 1
    print(index)
    num = 20151125
    for _ in range(index):
        num = get_next_number(num)

    return num


def q2():
    pass


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
