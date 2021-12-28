from dataclasses import dataclass


@dataclass
class Reindeer:
    speed: int
    fly_time: int
    rest_time: int

    def calc_distance(self, seconds: int) -> int:
        distance = 0
        while True:
            if seconds > self.fly_time + self.rest_time:
                seconds -= self.fly_time + self.rest_time
                distance += self.speed * self.fly_time
            elif seconds > self.fly_time:
                distance += self.speed * self.fly_time
                return distance
            else:
                distance += self.speed * seconds
                return distance


def parse_line(line: str) -> tuple[str, Reindeer]:
    # Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    name, _, _, speed, _, _, fly_time, _, _, _, _, _, _, rest_time, _ = line.split()
    return name, Reindeer(int(speed), int(fly_time), int(rest_time))


def q1(seconds):
    with open('day 14\input.txt', 'r') as f:
        input = f.read().splitlines()

    deers = dict()
    for line in input:
        name, reindeer = parse_line(line)
        deers[name] = reindeer

    return max(reindeer.calc_distance(seconds) for reindeer in deers.values())


def q2(seconds):
    with open('day 14\input.txt', 'r') as f:
        input = f.read().splitlines()

    deers = dict()
    for line in input:
        name, reindeer = parse_line(line)
        deers[name] = reindeer

    points = {name: 0 for name in deers}

    for second in range(seconds):
        best_deer = 'Comet'
        best_dist = deers[best_deer].calc_distance(second)
        for name, deer in deers.items():
            deer_dist = deer.calc_distance(second)
            if deer_dist > best_dist:
                best_deer = name
                best_dist = deer_dist

        points[best_deer] += 1

    return max(points.values())


if __name__ == '__main__':
    from time import perf_counter as pc
    st = pc()
    print(f'Part 1: {q1(2503)}')
    pt1 = pc()
    print(f'Part 2: {q2(2503)}')
    pt2 = pc()

    print(f'Time for execution:\n\
            Part 1: {(pt1-st)*1000}ms\n\
            Part 2: {(pt2-pt1)*1000}ms\n\
            Total: {(pt2-st)*1000}ms')
