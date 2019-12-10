INPUT = """1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1101,0,3,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1101,0,36,1015,1102,1,387,1028,1101,24,0,1016,1101,0,23,1008,1102,1,35,1012,1102,1,554,1023,1101,29,0,1003,1101,27,0,1011,1101,25,0,1000,1101,0,38,1018,1102,20,1,1019,1102,28,1,1005,1102,1,619,1026,1102,1,22,1004,1101,0,0,1020,1101,0,31,1009,1102,1,783,1024,1102,1,33,1001,1102,616,1,1027,1102,1,21,1006,1101,32,0,1013,1102,39,1,1014,1102,1,378,1029,1101,774,0,1025,1102,1,1,1021,1102,30,1,1007,1102,37,1,1002,1102,1,26,1017,1101,0,557,1022,1102,1,34,1010,109,13,2101,0,-5,63,1008,63,23,63,1005,63,203,4,187,1105,1,207,1001,64,1,64,1002,64,2,64,109,-14,2107,28,4,63,1005,63,225,4,213,1106,0,229,1001,64,1,64,1002,64,2,64,109,10,1207,-3,20,63,1005,63,245,1106,0,251,4,235,1001,64,1,64,1002,64,2,64,109,8,1205,3,263,1105,1,269,4,257,1001,64,1,64,1002,64,2,64,109,-9,1207,-7,34,63,1005,63,287,4,275,1105,1,291,1001,64,1,64,1002,64,2,64,109,-4,2102,1,-3,63,1008,63,32,63,1005,63,311,1105,1,317,4,297,1001,64,1,64,1002,64,2,64,109,21,21101,40,0,-6,1008,1019,43,63,1005,63,337,1106,0,343,4,323,1001,64,1,64,1002,64,2,64,109,-26,1202,7,1,63,1008,63,21,63,1005,63,365,4,349,1106,0,369,1001,64,1,64,1002,64,2,64,109,26,2106,0,3,4,375,1001,64,1,64,1105,1,387,1002,64,2,64,109,-9,21108,41,40,3,1005,1019,407,1001,64,1,64,1106,0,409,4,393,1002,64,2,64,109,13,1205,-8,423,4,415,1106,0,427,1001,64,1,64,1002,64,2,64,109,-19,21107,42,41,5,1005,1015,447,1001,64,1,64,1106,0,449,4,433,1002,64,2,64,109,-3,2102,1,-5,63,1008,63,37,63,1005,63,471,4,455,1105,1,475,1001,64,1,64,1002,64,2,64,109,-2,1201,0,0,63,1008,63,28,63,1005,63,497,4,481,1105,1,501,1001,64,1,64,1002,64,2,64,109,8,2107,29,-8,63,1005,63,521,1001,64,1,64,1106,0,523,4,507,1002,64,2,64,109,-3,1208,-3,30,63,1005,63,541,4,529,1106,0,545,1001,64,1,64,1002,64,2,64,109,4,2105,1,9,1105,1,563,4,551,1001,64,1,64,1002,64,2,64,109,9,1206,-3,581,4,569,1001,64,1,64,1106,0,581,1002,64,2,64,109,-8,1201,-9,0,63,1008,63,23,63,1005,63,605,1001,64,1,64,1106,0,607,4,587,1002,64,2,64,109,21,2106,0,-9,1106,0,625,4,613,1001,64,1,64,1002,64,2,64,109,-35,2108,31,8,63,1005,63,647,4,631,1001,64,1,64,1105,1,647,1002,64,2,64,109,2,1202,0,1,63,1008,63,30,63,1005,63,667,1105,1,673,4,653,1001,64,1,64,1002,64,2,64,109,17,21108,43,43,-4,1005,1016,691,4,679,1106,0,695,1001,64,1,64,1002,64,2,64,109,-14,1208,-1,30,63,1005,63,711,1106,0,717,4,701,1001,64,1,64,1002,64,2,64,109,6,21101,44,0,-1,1008,1011,44,63,1005,63,739,4,723,1105,1,743,1001,64,1,64,1002,64,2,64,109,-15,2108,30,8,63,1005,63,759,1106,0,765,4,749,1001,64,1,64,1002,64,2,64,109,27,2105,1,0,4,771,1001,64,1,64,1105,1,783,1002,64,2,64,109,-9,1206,6,795,1105,1,801,4,789,1001,64,1,64,1002,64,2,64,109,4,21102,45,1,-7,1008,1012,45,63,1005,63,823,4,807,1105,1,827,1001,64,1,64,1002,64,2,64,109,-14,21102,46,1,5,1008,1010,43,63,1005,63,851,1001,64,1,64,1105,1,853,4,833,1002,64,2,64,109,-1,2101,0,1,63,1008,63,25,63,1005,63,873,1105,1,879,4,859,1001,64,1,64,1002,64,2,64,109,9,21107,47,48,-3,1005,1010,897,4,885,1105,1,901,1001,64,1,64,4,64,99,21101,0,27,1,21101,915,0,0,1106,0,922,21201,1,57526,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21101,942,0,0,1106,0,922,21201,1,0,-1,21201,-2,-3,1,21101,957,0,0,1106,0,922,22201,1,-1,-2,1105,1,968,21202,-2,1,-2,109,-3,2106,0,0"""

# INPUT = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
# INPUT = "1102,34915192,34915192,7,4,7,99,0"
# INPUT = "104,1125899906842624,99"

INPUT = tuple(map(int, INPUT.strip().split(",")))


def parse_opcode(val):
    val = str(val).zfill(5)
    # opcode, 1st param mode, 2nd param mode, 3rd param mode
    return int(val[-2:]), int(val[-3]), int(val[-4]), int(val[-5])


POSITION_MODE = 0
IMMEDIATE_MODE = 1
RELATIVE_MODE = 2


def get_param(program, idx, mode, relative_base=0):
    if mode == POSITION_MODE:
        val_idx = program[idx]
    elif mode == RELATIVE_MODE:
        val_idx = relative_base + program[idx]
    else:
        # IMMEDIATE_MODE
        val_idx = idx
    return read(program, val_idx)


def get_res_idx(program, idx, mode, relative_base=0):
    val = get_param(program, idx, IMMEDIATE_MODE)
    if mode == RELATIVE_MODE:
        val += relative_base
    return val


def run_program(
    program_input, phase=1, input_val=1, opcode_idx=0, out=None, relative_base=0
):
    program = list(program_input)
    inp = phase
    while opcode_idx < len(program):
        opcode_raw = program[opcode_idx]
        opcode, param1_mode, param2_mode, param3_mode = parse_opcode(opcode_raw)
        # print(
        #     f"opcode at {opcode_idx}: {(opcode, param1_mode, param2_mode, param3_mode)}"
        # )
        # print_program(program)

        if opcode == 99:
            print("halt", out)
            return None, opcode_idx, out, relative_base, True

        # add
        if opcode == 1:
            arg1 = get_param(program, opcode_idx + 1, param1_mode, relative_base)
            arg2 = get_param(program, opcode_idx + 2, param2_mode, relative_base)

            res_idx = get_res_idx(program, opcode_idx + 3, param3_mode, relative_base)

            write(program, res_idx, arg1 + arg2)
            opcode_idx += 4
        # multiply
        elif opcode == 2:
            arg1 = get_param(program, opcode_idx + 1, param1_mode, relative_base)
            arg2 = get_param(program, opcode_idx + 2, param2_mode, relative_base)
            res_idx = get_res_idx(program, opcode_idx + 3, param3_mode, relative_base)
            write(program, res_idx, arg1 * arg2)
            opcode_idx += 4
        # input
        elif opcode == 3:

            res_idx = get_res_idx(program, opcode_idx + 1, param1_mode, relative_base)

            write(program, res_idx, inp)

            inp = input_val
            opcode_idx += 2
        # output
        elif opcode == 4:
            out = get_param(program, opcode_idx + 1, param1_mode, relative_base)
            opcode_idx += 2

            print("out", out)
            return program, opcode_idx, out, relative_base, False

        # jump-if-true
        elif opcode == 5:
            arg1 = get_param(program, opcode_idx + 1, param1_mode, relative_base)
            if arg1 != 0:
                opcode_idx = get_param(
                    program, opcode_idx + 2, param2_mode, relative_base
                )
            else:
                opcode_idx += 3
        # jump-if-false
        elif opcode == 6:
            arg1 = get_param(program, opcode_idx + 1, param1_mode, relative_base)
            if arg1 == 0:
                opcode_idx = get_param(
                    program, opcode_idx + 2, param2_mode, relative_base
                )
            else:
                opcode_idx += 3
        # less than
        elif opcode == 7:
            arg1 = get_param(program, opcode_idx + 1, param1_mode, relative_base)
            arg2 = get_param(program, opcode_idx + 2, param2_mode, relative_base)
            res_idx = get_res_idx(program, opcode_idx + 3, param3_mode, relative_base)
            write(program, res_idx, 1 if arg1 < arg2 else 0)
            opcode_idx += 4
        # equals
        elif opcode == 8:
            arg1 = get_param(program, opcode_idx + 1, param1_mode, relative_base)
            arg2 = get_param(program, opcode_idx + 2, param2_mode, relative_base)
            res_idx = get_res_idx(program, opcode_idx + 3, param3_mode, relative_base)
            write(program, res_idx, 1 if arg1 == arg2 else 0)
            opcode_idx += 4
        # adjusts the relative base
        elif opcode == 9:
            relative_base_offset = get_param(
                program, opcode_idx + 1, param1_mode, relative_base
            )
            relative_base += relative_base_offset
            # print("relative_base", param1_mode, relative_base_offset, relative_base)
            opcode_idx += 2
        else:
            print(f"bad opcode {opcode} at idx {opcode_idx}: {program}")
            break


def get_more_memory(program, idx):
    count = idx - len(program) + 1
    return [0] * count


def extend_program(program, idx):
    program.extend(get_more_memory(program, idx))
    return program


def write(program, idx, value):
    extend_program(program, idx)
    # print(f"write #{idx} = {value}")
    program[idx] = value


def read(program, idx):
    assert idx >= 0
    extend_program(program, idx)
    # print(f"read #{idx} = {program[idx]}")
    return program[idx]


def print_program(p, step=10):
    for idx in range(0, len(p), step):
        line = ", ".join(map(str, p[idx : idx + step]))
        print(f"[{idx} : {idx+step-1}]: {line}")


def run():
    res = []
    program_input = INPUT
    opcode_idx = 0
    out = None
    relative_base = 0
    while True:
        # print(opcode_idx, out, relative_base)
        program_input, opcode_idx, out, relative_base, is_halted = run_program(
            program_input,
            phase=2,
            input_val=2,
            opcode_idx=opcode_idx,
            out=out,
            relative_base=relative_base,
        )

        if is_halted:
            break

        res.append(out)

    print(",".join(map(str, res)))


if __name__ == "__main__":
    run()
