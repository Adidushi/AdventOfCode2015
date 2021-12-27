def is_nice(string: str) -> bool:

    has_vowels, has_gross, has_double = False, False, False

    vowel_counter = sum(string.count(vowel) for vowel in 'aeiou')
    if vowel_counter >= 3:
        has_vowels = True

    if 'ab' in string or 'cd' in string or 'pq' in string or 'xy' in string:
        has_gross = True

    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if f'{letter}{letter}' in string:
            has_double = True
            break

    return has_vowels and has_double and not has_gross


def q1():
    with open('day 05\input.txt', 'r') as f:
        input = f.read().splitlines()

    return sum(is_nice(s) for s in input)


def is_nice_2(string: str) -> bool:
    has_middle, has_pair = False, False

    for index in range(len(string[:-2])):
        if string[index] == string[index + 2]:
            has_middle = True
            break

    for pair in zip(string, string[1:]):
        pair = ''.join(pair)
        if pair in string.replace(pair, '_', 1):
            has_pair = True
            break

    if has_middle and has_pair:
        print(f'String: {string}, pair: {pair}')

    return has_middle and has_pair


def q2():
    with open('day 05\input.txt', 'r') as f:
        input = f.read().splitlines()

    return sum(is_nice_2(s) for s in input)


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
