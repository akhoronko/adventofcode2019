import math
from collections import defaultdict
from functools import partial
from itertools import cycle, chain

INPUT = """
.#......##.#..#.......#####...#..
...#.....##......###....#.##.....
..#...#....#....#............###.
.....#......#.##......#.#..###.#.
#.#..........##.#.#...#.##.#.#.#.
..#.##.#...#.......#..##.......##
..#....#.....#..##.#..####.#.....
#.............#..#.........#.#...
........#.##..#..#..#.#.....#.#..
.........#...#..##......###.....#
##.#.###..#..#.#.....#.........#.
.#.###.##..##......#####..#..##..
.........#.......#.#......#......
..#...#...#...#.#....###.#.......
#..#.#....#...#.......#..#.#.##..
#.....##...#.###..#..#......#..##
...........#...#......#..#....#..
#.#.#......#....#..#.....##....##
..###...#.#.##..#...#.....#...#.#
.......#..##.#..#.............##.
..###........##.#................
###.#..#...#......###.#........#.
.......#....#.#.#..#..#....#..#..
.#...#..#...#......#....#.#..#...
#.#.........#.....#....#.#.#.....
.#....#......##.##....#........#.
....#..#..#...#..##.#.#......#.#.
..###.##.#.....#....#.#......#...
#.##...#............#..#.....#..#
.#....##....##...#......#........
...#...##...#.......#....##.#....
.#....#.#...#.#...##....#..##.#.#
.#.#....##.......#.....##.##.#.##
"""

# (8, 3)
# INPUT = """
# .#....#####...#..
# ##...##.#####..##
# ##...#...#.#####.
# ..#.....#...###..
# ..#.#.....#....##
# """

# (11, 13)
# INPUT = """
# .#..##.###...#######
# ##.############..##.
# .#.######.########.#
# .###.#######.####.#.
# #####.##.#.##.###.##
# ..#####..#.#########
# ####################
# #.####....###.#.#.##
# ##.#################
# #####.##.###..####..
# ..######..##.#######
# ####.##.####...##..#
# .#####..#.######.###
# ##...#.##########...
# #.##########.#######
# .####.#.###.###.#.##
# ....##.##.###..#####
# .#.#.###########.###
# #.#.#.#####.####.###
# ###.##.####.##.#..##
# """

INPUT = tuple(tuple(row) for row in INPUT.strip().splitlines())


def run():
    asteroids = []
    for y, row in enumerate(INPUT):
        for x, p in enumerate(row):
            if p == "#":
                asteroids.append((x, y))

    crossings = defaultdict(lambda: defaultdict(list))
    for a1 in asteroids:
        for a2 in asteroids:
            if a1 == a2:
                continue
            crossings[a1][angle(a1, a2)].append(a2)

    best_asteroid, angles = max(crossings.items(), key=lambda item: len(item[1]))

    print(best_asteroid, len(angles))

    for same_angles in angles.values():
        same_angles.sort(key=partial(manhattan, best_asteroid), reverse=True)

    quadrant1 = []
    quadrant2 = []
    quadrant3 = []
    quadrant4 = []
    for dx, dy in angles:
        a = (dx, dy)
        if dx >= 0 and dy < 0:
            quadrant1.append(a)
        elif dx > 0 and dy >= 0:
            quadrant2.append(a)
        elif dx <= 0 and dy > 0:
            quadrant3.append(a)
        else:
            quadrant4.append(a)

    quadrant1.sort(key=lambda a: a[0] / a[1], reverse=True)

    print("quadrant1", len(quadrant1))
    for a in quadrant1:
        print(a, angles[a])

    quadrant2.sort(key=lambda a: a[1] / a[0])

    print("quadrant2", len(quadrant1) + len(quadrant2))
    for a in quadrant2:
        print(a, angles[a])

    quadrant3.sort(key=lambda a: a[0] / a[1], reverse=True)

    print("quadrant3", len(quadrant1) + len(quadrant2) + len(quadrant3))
    for a in quadrant3:
        print(a, angles[a])

    quadrant4.sort(key=lambda a: a[1] / a[0])

    print(
        "quadrant4", len(quadrant1) + len(quadrant2) + len(quadrant3) + len(quadrant4)
    )
    for a in quadrant4:
        print(a, angles[a])

    sorted_angles = []
    for q in [quadrant1, quadrant2, quadrant3, quadrant4]:
        sorted_angles.extend(q)

    max_vaporized_count = sum(len(angles[a]) for a in sorted_angles)

    vaporized_count = 0
    for a in cycle(sorted_angles):
        targets = angles[a]
        if not targets:
            print("no more targets: ", a)
            continue

        vaporized = targets.pop()
        vaporized_count += 1

        print(f"#{vaporized_count}: {vaporized}")

        if vaporized_count == 200 or vaporized_count == max_vaporized_count:
            break


def coord_deltas(a1, a2):
    x1, y1 = a1
    x2, y2 = a2
    dx = x2 - x1
    dy = y2 - y1
    return dx, dy


def angle(a1, a2):
    dx, dy = coord_deltas(a1, a2)
    gcd = math.gcd(dx, dy)
    if gcd:
        dx = dx // gcd
        dy = dy // gcd

    return dx, dy


def manhattan(a1, a2):
    dx, dy = coord_deltas(a1, a2)
    return abs(dx) + abs(dy)


if __name__ == "__main__":
    run()
