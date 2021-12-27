from hashlib import md5


def q1():
    with open('day 04\input.txt', 'r') as f:
        input = f.read().strip()

    current_num = 0

    while True:
        to_test = input+str(current_num)
        hashed = md5(to_test.encode()).hexdigest()
        if hashed.startswith('00000'):
            return current_num
        current_num += 1


def q2():
    with open('day 04\input.txt', 'r') as f:
        input = f.read().strip()

    current_num = 0

    while True:
        to_test = input+str(current_num)
        hashed = md5(to_test.encode()).hexdigest()
        if hashed.startswith('000000'):
            return current_num
        current_num += 1


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
