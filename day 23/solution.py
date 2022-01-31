def interpret_command(a, b, index, input):
    command = input[index].split()
    match command[0]:
        case 'inc':
            arg = command[1]
            if arg == 'a':
                a += 1
            elif arg == 'b':
                b += 1
            index += 1
        case 'hlf':
            arg = command[1]
            if arg == 'a':
                a //= 2
            elif arg == 'b':
                b //= 2
            index += 1
        case 'tpl':
            arg = command[1]
            if arg == 'a':
                a *= 3
            elif arg == 'b':
                b *= 3
            index += 1
        case 'jmp':
            offset = int(command[1])
            index += offset
        case 'jie':
            arg = command[1]
            offset = int(command[2])
            if arg == 'a':
                if a % 2 == 0:
                    index += offset
                else:
                    index += 1
            elif arg == 'b':
                if b % 2 == 0:
                    index += offset
                else:
                    index += 1

        case 'jio':
            arg = command[1]
            offset = int(command[2])
            if arg == 'a':
                if a == 1:
                    index += offset
                else:
                    index += 1
            elif arg == 'b':
                if b == 1:
                    index += offset
                else:
                    index += 1
    return a, b, index


def q1():
    with open('day 23\input.txt', 'r') as f:
        input = f.read().splitlines()

    index, a, b = 0, 0, 0
    while 0 <= index < len(input):
        a, b, index = interpret_command(a, b, index, input)
    return b


def q2():
    with open('day 23\input.txt', 'r') as f:
        input = f.read().splitlines()

    index, a, b = 0, 1, 0
    while 0 <= index < len(input):
        a, b, index = interpret_command(a, b, index, input)
    return b


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
