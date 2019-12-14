INPUT = """
1 JKXFH => 8 KTRZ
11 TQGT, 9 NGFV, 4 QZBXB => 8 MPGLV
8 NPDPH, 1 WMXZJ => 7 VCNSK
1 MPGLV, 6 CWHX => 5 GDRZ
16 JDFQZ => 2 CJTB
1 GQNQF, 4 JDFQZ => 5 WJKDC
2 TXBS, 4 SMGQW, 7 CJTB, 3 NTBQ, 13 CWHX, 25 FLPFX => 1 FUEL
3 WMXZJ, 14 CJTB => 5 FLPFX
7 HDCTQ, 1 MPGLV, 2 VFVC => 1 GSVSD
1 WJKDC => 2 NZSQR
1 RVKLC, 5 CMJSL, 16 DQTHS, 31 VCNSK, 1 RKBMX, 1 GDRZ => 8 SMGQW
2 JDFQZ, 2 LGKHR, 2 NZSQR => 9 TSWN
34 LPXW => 8 PWJFD
2 HDCTQ, 2 VKWN => 8 ZVBRF
2 XCTF => 3 QZBXB
12 NGFV, 3 HTRWR => 5 HDCTQ
1 TSWN, 2 WRSD, 1 ZVBRF, 1 KFRX, 5 BPVMR, 2 CLBG, 22 NPSLQ, 9 GSVSD => 5 NTBQ
10 TSWN => 9 VFVC
141 ORE => 6 MKJDZ
4 NPSLQ, 43 VCNSK, 4 PSJL, 14 KTRZ, 3 KWCDP, 3 HKBS, 11 WRSD, 3 MXWHS => 8 TXBS
8 VCNSK, 1 HDCTQ => 7 MXWHS
3 JDFQZ, 2 GQNQF => 4 XJSQW
18 NGFV, 4 GSWT => 5 KFRX
2 CZSJ => 7 GMTW
5 PHKL, 5 VCNSK, 25 GSVSD => 8 FRWC
30 FRWC, 17 GKDK, 8 NPSLQ => 3 CLBG
8 MXWHS, 3 SCKB, 2 NPSLQ => 1 JKXFH
1 XJSQW, 7 QZBXB => 1 LGKHR
115 ORE => 6 GQNQF
12 HTRWR, 24 HDCTQ => 1 RKBMX
1 DQTHS, 6 XDFWD, 1 MXWHS => 8 VKWN
129 ORE => 3 XCTF
6 GQNQF, 7 WJKDC => 5 PHKL
3 NZSQR => 2 LPXW
2 FLPFX, 1 MKLP, 4 XDFWD => 8 NPSLQ
4 DQTHS, 1 VKWN => 1 BPVMR
7 GMTW => 1 TXMVX
152 ORE => 8 JDFQZ
21 LGKHR => 9 NPDPH
5 CJTB, 1 QZBXB, 3 KFRX => 1 GTPB
1 MXWHS => 3 CWHX
3 PHKL => 1 NGFV
1 WMXZJ => 7 XDFWD
3 TSWN, 1 VKWN => 8 GKDK
1 ZVBRF, 16 PWJFD => 8 CMJSL
3 VCNSK, 7 GDRZ => 4 HKBS
20 XJSQW, 6 HTRWR, 7 CJTB => 5 WMXZJ
12 ZVBRF, 10 FRWC, 12 TSWN => 4 WRSD
16 HDCTQ, 3 GTPB, 10 NGFV => 4 KWCDP
3 TXMVX, 1 NPDPH => 8 HTRWR
9 NPDPH, 6 LPXW => 8 GSWT
4 MKLP => 1 TQGT
34 GTPB => 3 RVKLC
25 VFVC, 5 RVKLC => 8 DQTHS
7 KWCDP => 3 SCKB
6 LGKHR => 8 MKLP
39 MKJDZ => 9 CZSJ
2 TSWN, 1 WMXZJ => 3 PSJL
"""


def parse_item(s):
    amount, name = s.split(" ")
    return int(amount), name


def parse_input(input_raw):
    inp = []
    for equation in input_raw.strip().splitlines():
        parts, res = [s.strip() for s in equation.split("=>")]
        res = parse_item(res)
        parts = [parse_item(s.strip()) for s in parts.split(", ")]
        inp.append((tuple(parts), res))
    return tuple(inp)


def get_element(elements, balance, direct, amount, name):
    # print(f"get_element({amount}, {name})")

    # deficit = amount - balance[name]

    while balance[name] < amount:
        amount_delta, parts = elements[name]

        if name in direct:
            ore_amount = parts[0][0]
            new_ore_amount = balance["ORE"] - ore_amount
            # print(f"ORE: {balance['ORE']} - {ore_amount} => {new_ore_amount}")
            balance["ORE"] = new_ore_amount
        else:
            for part_amount, part_name in parts:
                balance = get_element(elements, balance, direct, part_amount, part_name)

        new_amount = balance[name] + amount_delta
        # print(f"{name}: {balance[name]} + {amount_delta} => {new_amount}")
        balance[name] = new_amount

    new_amount = balance[name] - amount
    # print(f"{name}: {balance[name]} - {amount} => {new_amount}")
    balance[name] = new_amount

    return balance


def run():
    inp = parse_input(INPUT)

    assert len(set(res[1] for _, res in inp)) == len(inp)

    elements = {}
    direct = set()
    for parts, (res_amount, res_name) in inp:
        elements[res_name] = (res_amount, parts)

        if len(parts) == 1 and parts[0][1] == "ORE":
            direct.add(res_name)

    max_ore = 1000000000000

    balance = {n: 0 for n in elements}
    balance["ORE"] = max_ore

    # weird bruteforce
    fuel_count = 0
    while True:
        balance = get_element(elements, balance, direct, 1, "FUEL")
        print(balance["ORE"])
        if balance["ORE"] >= 0:
            fuel_count += 1
        else:
            break

    print("end", fuel_count)


if __name__ == "__main__":
    run()
