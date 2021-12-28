import json


def scan_json_object(json_object):
    values = list()
    if isinstance(json_object, list):
        for thing in json_object:
            if isinstance(thing, int):
                values.append(thing)
            elif isinstance(thing, (dict, list)):
                values.extend(scan_json_object(thing))
    if isinstance(json_object, dict):
        for thing in json_object.values():
            if isinstance(thing, int):
                values.append(thing)
            elif isinstance(thing, (dict, list)):
                values.extend(scan_json_object(thing))
    return values


def scan_json_object_2(json_object):
    values = list()
    if isinstance(json_object, list):
        for thing in json_object:
            if isinstance(thing, int):
                values.append(thing)
            elif isinstance(thing, (dict, list)):
                values.extend(scan_json_object_2(thing))
    if isinstance(json_object, dict):
        if 'red' not in json_object.values() and 'red' not in json_object.keys():
            for thing in json_object.values():
                if isinstance(thing, int):
                    values.append(thing)
                elif isinstance(thing, (dict, list)):
                    values.extend(scan_json_object_2(thing))
    return values


def q1():
    with open('day 12\input.txt', 'r') as f:
        input = json.load(f)

    values = list()
    for thing in input.values():
        values.extend(scan_json_object(thing))

    return sum(values)


def q2():
    with open('day 12\input.txt', 'r') as f:
        input = json.load(f)

    values = list()
    for thing in input.values():
        values.extend(scan_json_object_2(thing))

    return sum(values)


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
