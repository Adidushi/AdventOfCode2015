def q1():
    with open('day 08\input.txt', 'r') as f:
        input = f.read()
    all_chars = len(input.replace('\n', '').strip())

    length = 0
    for line in input.splitlines():
        length += len(eval(line))
    
    return(all_chars-length)

def encod(line: str) -> int:
    line = line.replace('\\', '\\\\')
    line = line.replace('"', '\\"')
    return len(line) + 2

    
def q2():
    with open('day 08\input.txt', 'r') as f:
        input = f.read()
    orig_chars = len(input.replace('\n', '').strip())

    length = 0
    for line in input.splitlines():
        length += encod(line)
    
    return(length - orig_chars)

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