def q1():
    with open('day 07\input.txt', 'r') as f:
        input = f.read().splitlines()

    final_program = ''
    for line in sorted(input):
        line = line.split()
        output = line[-1]
        if 'AND' in line:
            first = line[0]
            second = line[2]
            final_program += f'{output} = {first} & {second}'
        elif 'OR' in line:
            first = line[0]
            second = line[2]
            final_program += f'{output} = {first} | {second}'
        elif 'NOT' in line:
            in_reg = line[1]
            final_program += f'{output} = ~{in_reg}'
        elif 'LSHIFT' in line:
            in_reg = line[0]
            shift_amt = line[2]
            final_program += f'{output} = {in_reg} << {shift_amt}'
        elif 'RSHIFT' in line:
            in_reg = line[0]
            shift_amt = line[2]
            final_program += f'{output} = {in_reg} >> {shift_amt}'
        else:
            in_reg = line[0]
            final_program += f'{output} = {in_reg}'

        final_program += '\n'
    
    lines = sorted(final_program.splitlines())


    with open('day 07\out_file.py', 'w') as f:
        f.write('\n'.join(lines))



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
