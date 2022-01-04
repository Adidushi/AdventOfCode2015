
def parse_sue(line):
    name, *values = line.split(':')
    values = map(str.strip, ':'.join(values).strip().split(','))
    sue = dict()
    for value in values:
        k, v = map(str.strip, value.split(':'))
        sue[k] = int(v)
    return {name: sue}


def q1():
    with open('day 16\input.txt', 'r') as f:
        input = f.read().splitlines()
    sues = dict()
    for line in input:
        sues.update(parse_sue(line))
    
    requirements = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }

    good_sues = dict(sues)

    for k, v in requirements.items():
        good_sues = dict()
        for sue, sue_items in sues.items():
            if k in sue_items and sue_items[k] == v or k not in sue_items:
                good_sues[sue] = sue_items
        sues = good_sues
    
    return list(good_sues.keys())[0]

    
def q2():
    with open('day 16\input.txt', 'r') as f:
        input = f.read().splitlines()
    sues = dict()
    for line in input:
        sues.update(parse_sue(line))
    
    requirements = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }

    good_sues = dict(sues)

    for k, v in requirements.items():
        good_sues = dict()
        for sue, sue_items in sues.items():
            if k in ('cats', 'trees') and k in sue_items and sue_items[k] > v or k not in sue_items:
                good_sues[sue] = sue_items
            elif k in ('pomeranians', 'goldfish') and k in sue_items and sue_items[k] < v or k not in sue_items:
                good_sues[sue] = sue_items
            elif k not in ('cats', 'trees', 'pomeranians', 'goldfish') and k in sue_items and sue_items[k] == v or k not in sue_items:
                good_sues[sue] = sue_items
        sues = good_sues
    
    return list(good_sues.keys())[0]

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