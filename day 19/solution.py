import re
from dataclasses import dataclass


def replacenth(string, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, string)][n-1]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    newString = before + after
    return newString


def parse(input):
    replacements, molecule = input.split('\n\n')

    replacement_dict = dict()
    for replacement in replacements.splitlines():
        original, new = replacement.split(' => ')
        if original not in replacement_dict:
            replacement_dict[original] = list()
        replacement_dict[original].append(new)

    return replacement_dict, molecule


def parse_into_tuples(input):
    replacements, molecule = input.split('\n\n')
    replacements = [replacement.split(' => ')
                    for replacement in replacements.splitlines()]
    return replacements, molecule


@dataclass
class MoleculeState:
    molecule: str
    steps: int

    def replace_all(self, replacements):
        new_molecules = set()
        for original, news in replacements.items():
            count = self.molecule.count(original)
            for new in news:
                for i in range(0, count):
                    new_molecules.add(replacenth(
                        self.molecule, original, new, i))

        for molecule in new_molecules:
            yield(MoleculeState(molecule, self.steps + 1))


def q1():
    with open('day 19\input.txt', 'r') as f:
        input = f.read()
    replacements, molecule = parse(input)

    new_molecules = set()

    for original, news in replacements.items():
        count = molecule.count(original)
        for new in news:
            for i in range(0, count):
                new_molecules.add(replacenth(molecule, original, new, i))

    return len(new_molecules)


def q2():
    with open('day 19\input.txt', 'r') as f:
        input = f.read()
    replacements, molecule = parse_into_tuples(input)

    steps = 0
    while molecule != 'e':
        for original, new in replacements:
            if new in molecule:
                molecule = molecule.replace(new, original, 1)
                steps += 1
    return steps


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
