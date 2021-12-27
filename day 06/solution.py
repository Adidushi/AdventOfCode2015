from dataclasses import dataclass
import numpy as np

@dataclass
class Instruction:
    cmd: str
    rs: tuple[int, int]
    cs: tuple[int, int]

    def iterate(self):
        min_r, max_r = sorted(self.rs)
        min_c, max_c = sorted(self.cs)
        for r in range(min_r, max_r+1):
            for c in range(min_c, max_c+1):
                yield((r, c))
            

def parse(input: list[str]) -> list[Instruction]:
    commands = list()
    for line in input:
        line = line.replace('turn ', '')
        line = line.split()
        cmd = line[0]

        start = line[1].split(',')
        start_r, start_c = start

        end = line[-1].split(',')
        end_r, end_c = end

        rows = (int(start_r), int(end_r))
        cols = (int(start_c), int(end_c))

        commands.append(Instruction(cmd, rows, cols))

    return commands

def execute(instruction: Instruction, lights):
    match instruction.cmd:
        case 'on':
            for r, c in instruction.iterate():
                lights[r][c] = True
        case 'off':
            for r, c in instruction.iterate():
                lights[r][c] = False
        case 'toggle':
            for r, c in instruction.iterate():
                lights[r][c] = not lights[r][c]
    return lights

def q1():
    with open('day 06\input.txt', 'r') as f:
        input = f.read().splitlines()
    input = parse(input)

    lights = np.zeros((1000, 1000), dtype=bool)
    for cmd in input:
        lights = execute(cmd, lights)
    
    return lights.sum()

def execute_2(instruction: Instruction, lights):
    match instruction.cmd:
        case 'on':
            for r, c in instruction.iterate():
                lights[r][c] += 1
        case 'off':
            for r, c in instruction.iterate():
                lights[r][c] -= 1 if lights[r][c] > 0 else 0
        case 'toggle':
            for r, c in instruction.iterate():
                lights[r][c] += 2
    return lights

    
def q2():
    with open('day 06\input.txt', 'r') as f:
        input = f.read().splitlines()
    input = parse(input)

    lights = np.zeros((1000, 1000), dtype=np.int16)
    for cmd in input:
        lights = execute_2(cmd, lights)
    
    return lights.sum()

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