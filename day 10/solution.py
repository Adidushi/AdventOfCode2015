from itertools import groupby

def expand(num: int) -> int:
    counter = 1
    current_digit = num % 10
    num //= 10

    expanded_num = ''

    while num > 0:
        
        if num % 10 == current_digit:
            counter += 1
        else:
            expanded_num = f'{counter}{current_digit}{expanded_num}'
            counter = 0
            current_digit = num % 10
        num //= 10
        

    expanded_num = f'{counter}{current_digit}{expanded_num}'
    
    return int(expanded_num)

def better_expand(num: str) -> str:
    num = [''.join(n) for _, n in groupby(num)]
    out_str = ''
    for ch in num:
        out_str += str(len(ch))
        out_str += ch[0]
    return out_str

def q1(iterations, input):

    for _ in range(iterations):
        # print(input)
        input = better_expand(input)

    return len(input)

    
def q2():
    input = 3113322113

if __name__ == '__main__':
    from time import perf_counter as  pc
    st = pc()
    print(f'Part 1: {q1(40, "3113322113")}') #3113322113
    pt1 = pc()
    print(f'Part 2: {q1(50, "3113322113")}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 1: {(pt1-st)*1000}ms\n\
            Part 2: {(pt2-pt1)*1000}ms\n\
            Total: {(pt2-st)*1000}ms')