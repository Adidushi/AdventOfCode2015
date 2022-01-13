from math import sqrt
from functools import cache

@cache
def generate_divisors(n):
    small_divisors = [i for i in range(1, int(sqrt(n)) + 1) if n % i == 0]
    large_divisors = [n / d for d in small_divisors if n != d * d]
    return small_divisors + large_divisors

@cache
def calc_presents(house_num):
    return sum(10 * elf for elf in generate_divisors(house_num))

@cache
def calc_some_presents(house_num):
    return sum(11 * elf for elf in generate_divisors(house_num) if house_num / elf <= 50)

def q1(amount_of_presents):
    house_num = 1
    while True:
        if calc_presents(house_num) >= amount_of_presents:
            return house_num
        house_num += 1
    
def q2(amount_of_presents):
    house_num = 1
    while True:
        if calc_some_presents(house_num) >= amount_of_presents:
            return house_num
        house_num += 1


if __name__ == '__main__':
    from time import perf_counter as  pc
    st = pc()
    print(f'Part 1: {q1(33100000)}')
    pt1 = pc()
    print(f'Part 2: {q2(33100000)}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 1: {(pt1-st)*1000}ms\n\
            Part 2: {(pt2-pt1)*1000}ms\n\
            Total: {(pt2-st)*1000}ms')