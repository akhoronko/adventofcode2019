from itertools import combinations

INPUT = """
<x=17, y=-12, z=13>
<x=2, y=1, z=1>
<x=-1, y=-17, z=7>
<x=12, y=-14, z=18>
"""

# INPUT = """
# <x=-1, y=0, z=2>
# <x=2, y=-10, z=-7>
# <x=4, y=-8, z=8>
# <x=3, y=5, z=-1>
# """

INPUT = tuple(
    tuple(int(x.split("=")[1]) for x in s[1:-1].split(", "))
    for s in INPUT.strip().splitlines()
)


def velocity_deltas(v1, v2):
    if v1 > v2:
        return -1, 1
    elif v1 < v2:
        return 1, -1
    return 0, 0


def print_moons(step, moons):
    print(f"After {step} step:")
    for pos, vel in moons:
        print(
            f"pos=<x={pos[0]}, y={pos[1]}, z={pos[2]}>, "
            f"vel=<x={vel[0]}, y={vel[1]}, z={vel[2]}>"
        )
    print(f"Total energy: {total_energy(moons)}")


def pot_energy(m):
    pos, vel = m
    return sum(map(abs, pos))


def kin_energy(m):
    pos, vel = m
    return sum(map(abs, vel))


def total_energy(moons):
    return sum(pot_energy(m) * kin_energy(m) for m in moons)


def run(steps_count=1000):
    # <pos>, <vel>
    moons = [(list(pos), [0] * 3) for pos in INPUT]
    print_moons(0, moons)
    for step in range(1, steps_count + 1):
        # apply gravity
        for (pos1, vel1), (pos2, vel2) in combinations(moons, 2):
            deltas = [velocity_deltas(p1, p2) for p1, p2 in zip(pos1, pos2)]
            for idx, (d1, d2) in enumerate(deltas):
                vel1[idx] += d1
                vel2[idx] += d2
        # apply gravity
        for pos, vel in moons:
            for idx, v in enumerate(vel):
                pos[idx] += v
        print_moons(step, moons)


if __name__ == "__main__":
    run()
