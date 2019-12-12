from itertools import combinations
from math import gcd

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

# INPUT = """
# <x=-8, y=-10, z=0>
# <x=5, y=5, z=10>
# <x=2, y=-7, z=3>
# <x=9, y=-8, z=-3>
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


def copy_moons(moons):
    return tuple((tuple(pos), tuple(vel)) for pos, vel in moons)


def run(steps_count=1000000):
    # <pos>, <vel>
    moons = [(list(pos), [0] * 3) for pos in INPUT]
    step = 0
    print_moons(step, moons)

    states = []

    while True:
        states.append(copy_moons(moons))

        step += 1

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

        # print_moons(step, moons)

        if step == steps_count:
            print("break")
            break

    moon_lcm_values = []
    for moon_idx in range(len(moons)):
        pos_periods = [
            find_period(states, moon_idx, True, coord_idx) for coord_idx in range(3)
        ]
        vel_periods = [
            find_period(states, moon_idx, False, coord_idx) for coord_idx in range(3)
        ]
        moon_lcm = lcm(pos_periods + vel_periods)
        print(moon_idx, pos_periods, vel_periods, moon_lcm)
        moon_lcm_values.append(moon_lcm)

    print(lcm(moon_lcm_values))


def find_period(states, moon_idx, is_pos, coord_idx):
    vals = []
    for moons in states:
        moon = moons[moon_idx]
        source = moon[0] if is_pos else moon[1]
        vals.append(source[coord_idx])

    init = vals[0]
    res = []
    for step, x in enumerate(vals):
        if init == x:
            res.append(step)

    d = [b - a for a, b in zip(res, res[1:])]
    for i in range(1, len(d) // 2 + 1):
        if not len(set(d[0:i])) == 1 and d[0:i] == d[i : i * 2]:
            return sum(d[:i])


def lcm(l):
    res = l[0]
    for i in l[1:]:
        res = int(res * i // gcd(res, i))
    return res


if __name__ == "__main__":
    run()
