INPUT = "3,225,1,225,6,6,1100,1,238,225,104,0,1101,65,73,225,1101,37,7,225,1101,42,58,225,1102,62,44,224,101,-2728,224,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,1,69,126,224,101,-92,224,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,1102,41,84,225,1001,22,92,224,101,-150,224,224,4,224,102,8,223,223,101,3,224,224,1,224,223,223,1101,80,65,225,1101,32,13,224,101,-45,224,224,4,224,102,8,223,223,101,1,224,224,1,224,223,223,1101,21,18,225,1102,5,51,225,2,17,14,224,1001,224,-2701,224,4,224,1002,223,8,223,101,4,224,224,1,223,224,223,101,68,95,224,101,-148,224,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1102,12,22,225,102,58,173,224,1001,224,-696,224,4,224,1002,223,8,223,1001,224,6,224,1,223,224,223,1002,121,62,224,1001,224,-1302,224,4,224,1002,223,8,223,101,4,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,226,677,224,102,2,223,223,1005,224,329,1001,223,1,223,7,677,226,224,102,2,223,223,1006,224,344,1001,223,1,223,1007,226,677,224,1002,223,2,223,1006,224,359,1001,223,1,223,1007,677,677,224,102,2,223,223,1005,224,374,1001,223,1,223,108,677,677,224,102,2,223,223,1006,224,389,101,1,223,223,8,226,677,224,102,2,223,223,1005,224,404,101,1,223,223,7,226,677,224,1002,223,2,223,1005,224,419,101,1,223,223,8,677,226,224,1002,223,2,223,1005,224,434,101,1,223,223,107,677,677,224,1002,223,2,223,1006,224,449,101,1,223,223,7,677,677,224,1002,223,2,223,1006,224,464,101,1,223,223,1107,226,226,224,102,2,223,223,1006,224,479,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,494,101,1,223,223,108,226,677,224,1002,223,2,223,1006,224,509,101,1,223,223,1108,226,677,224,102,2,223,223,1006,224,524,1001,223,1,223,1008,226,226,224,1002,223,2,223,1005,224,539,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,554,101,1,223,223,8,677,677,224,102,2,223,223,1005,224,569,101,1,223,223,107,226,677,224,102,2,223,223,1005,224,584,101,1,223,223,1108,226,226,224,1002,223,2,223,1005,224,599,1001,223,1,223,1008,677,677,224,1002,223,2,223,1005,224,614,101,1,223,223,1107,226,677,224,102,2,223,223,1005,224,629,101,1,223,223,1108,677,226,224,1002,223,2,223,1005,224,644,1001,223,1,223,1107,677,226,224,1002,223,2,223,1006,224,659,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,674,101,1,223,223,4,223,99,226"
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


def run_program(inp=5):
    program = list(INPUT)
    opcode_idx = 0
    out = 0
    while opcode_idx < len(program):
        opcode_raw = program[opcode_idx]
        opcode, param1_mode, param2_mode, param3_mode = parse_opcode(opcode_raw)
        print(
            f"opcode at {opcode_idx}: {(opcode, param1_mode, param2_mode, param3_mode)}"
        )

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


def print_program(p, step=10):
    for idx in range(0, len(p), step):
        line = ", ".join(map(str, p[idx:idx+step]))
        print(f"[{idx} : {idx+step-1}]: {line}")


def run():
    run_program()


if __name__ == "__main__":
    run()