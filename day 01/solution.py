def q1():
    with open('day 01\input.txt', 'r') as f:
        input = f.read()

    return input.count('(') - input.count(')')
    
def q2():
    with open('day 01\input.txt', 'r') as f:
        input = f.read()

    floor = 0
    index = 0
    while floor != -1:
        floor += 1 if input[index] == '(' else -1
        index += 1
    return index


if __name__ == '__main__':
    from time import perf_counter as  pc
    st = pc()
    print(f'Part 1: {q1()}')
    pt1 = pc()
    print(f'Part 2: {q2()}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 1: {(pt1-st)*1000}ms\n\
            Part 2: {(pt2-pt1)*1000}ms\n\
            Total: {(pt2-st)*1000}ms')