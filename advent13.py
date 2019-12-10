from itertools import permutations

INPUT = """3,8,1001,8,10,8,105,1,0,0,21,42,67,84,109,126,207,288,369,450,99999,3,9,102,4,9,9,1001,9,4,9,102,2,9,9,101,2,9,9,4,9,99,3,9,1001,9,5,9,1002,9,5,9,1001,9,5,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,101,5,9,9,1002,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,102,4,9,9,101,2,9,9,102,4,9,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,101,5,9,9,1002,9,2,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,99"""

INPUT = tuple(map(int, INPUT.split(",")))


def parse_opcode(val):
    val = str(val).zfill(5)
    # opcode, 1st param mode, 2nd param mode, 3rd param mode
    return int(val[-2:]), int(val[-3]), int(val[-4]), int(val[-5])


POSITION_MODE = 0
IMMEDIATE_MODE = 1


def get_param(program, idx, mode):
    if mode == POSITION_MODE:
        return program[program[idx]]
    else:
        # IMMEDIATE_MODE
        return program[idx]


def run_program(program_input, phase, input):
    program = list(program_input)
    opcode_idx = 0
    out = 0
    inp = phase
    while opcode_idx < len(program):
        opcode_raw = program[opcode_idx]
        opcode, param1_mode, param2_mode, param3_mode = parse_opcode(opcode_raw)
        # print(
        #     f"opcode at {opcode_idx}: {(opcode, param1_mode, param2_mode, param3_mode)}"
        # )

        # print_program(program)

        if opcode == 99:
            print("halt")
            break

        if out:
            print("bad output")
            break

        # add
        if opcode == 1:
            arg1 = get_param(program, opcode_idx + 1, param1_mode)
            arg2 = get_param(program, opcode_idx + 2, param2_mode)
            res_idx = get_param(program, opcode_idx + 3, IMMEDIATE_MODE)
            program[res_idx] = arg1 + arg2
            opcode_idx += 4
        # multiply
        elif opcode == 2:
            arg1 = get_param(program, opcode_idx + 1, param1_mode)
            arg2 = get_param(program, opcode_idx + 2, param2_mode)
            res_idx = get_param(program, opcode_idx + 3, IMMEDIATE_MODE)
            program[res_idx] = arg1 * arg2
            opcode_idx += 4
        # input
        elif opcode == 3:
            res_idx = get_param(program, opcode_idx + 1, IMMEDIATE_MODE)
            program[res_idx] = inp
            inp = input
            opcode_idx += 2
        # output
        elif opcode == 4:
            out = get_param(program, opcode_idx + 1, param1_mode)
            print(f"out: {out}")
            opcode_idx += 2
        # jump-if-true
        elif opcode == 5:
            arg1 = get_param(program, opcode_idx + 1, param1_mode)
            if arg1 != 0:
                opcode_idx = get_param(program, opcode_idx + 2, param2_mode)
            else:
                opcode_idx += 3
        # jump-if-false
        elif opcode == 6:
            arg1 = get_param(program, opcode_idx + 1, param1_mode)
            if arg1 == 0:
                opcode_idx = get_param(program, opcode_idx + 2, param2_mode)
            else:
                opcode_idx += 3
        # less than
        elif opcode == 7:
            arg1 = get_param(program, opcode_idx + 1, param1_mode)
            arg2 = get_param(program, opcode_idx + 2, param2_mode)
            res_idx = get_param(program, opcode_idx + 3, IMMEDIATE_MODE)
            program[res_idx] = 1 if arg1 < arg2 else 0
            opcode_idx += 4
        # equals
        elif opcode == 8:
            arg1 = get_param(program, opcode_idx + 1, param1_mode)
            arg2 = get_param(program, opcode_idx + 2, param2_mode)
            res_idx = get_param(program, opcode_idx + 3, IMMEDIATE_MODE)
            program[res_idx] = 1 if arg1 == arg2 else 0
            opcode_idx += 4
        else:
            print(f"bad opcode {opcode} at idx {opcode_idx}: {program}")
            break

    return out


def print_program(p, step=10):
    for idx in range(0, len(p), step):
        line = ", ".join(map(str, p[idx : idx + step]))
        print(f"[{idx} : {idx+step-1}]: {line}")


def run():
    phase_settings = permutations(range(5), 5)
    signals = []
    for phases in phase_settings:
        out = 0
        print(phases)
        for p in phases:
            out = run_program(INPUT, p, out)
        signals.append(out)
    print("max signal", max(signals))


if __name__ == "__main__":
    run()
