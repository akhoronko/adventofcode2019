INPUT = """1,380,379,385,1008,2311,194223,381,1005,381,12,99,109,2312,1101,0,0,383,1101,0,0,382,20102,1,382,1,21002,383,1,2,21101,0,37,0,1106,0,578,4,382,4,383,204,1,1001,382,1,382,1007,382,38,381,1005,381,22,1001,383,1,383,1007,383,22,381,1005,381,18,1006,385,69,99,104,-1,104,0,4,386,3,384,1007,384,0,381,1005,381,94,107,0,384,381,1005,381,108,1105,1,161,107,1,392,381,1006,381,161,1101,-1,0,384,1106,0,119,1007,392,36,381,1006,381,161,1101,0,1,384,21002,392,1,1,21101,0,20,2,21101,0,0,3,21102,138,1,0,1106,0,549,1,392,384,392,21002,392,1,1,21102,20,1,2,21102,1,3,3,21102,1,161,0,1106,0,549,1101,0,0,384,20001,388,390,1,20102,1,389,2,21102,180,1,0,1106,0,578,1206,1,213,1208,1,2,381,1006,381,205,20001,388,390,1,21002,389,1,2,21101,205,0,0,1105,1,393,1002,390,-1,390,1101,0,1,384,20101,0,388,1,20001,389,391,2,21102,228,1,0,1105,1,578,1206,1,261,1208,1,2,381,1006,381,253,21002,388,1,1,20001,389,391,2,21101,0,253,0,1106,0,393,1002,391,-1,391,1102,1,1,384,1005,384,161,20001,388,390,1,20001,389,391,2,21101,0,279,0,1106,0,578,1206,1,316,1208,1,2,381,1006,381,304,20001,388,390,1,20001,389,391,2,21102,304,1,0,1105,1,393,1002,390,-1,390,1002,391,-1,391,1101,1,0,384,1005,384,161,20101,0,388,1,21002,389,1,2,21101,0,0,3,21102,1,338,0,1106,0,549,1,388,390,388,1,389,391,389,20102,1,388,1,21001,389,0,2,21101,0,4,3,21101,365,0,0,1106,0,549,1007,389,21,381,1005,381,75,104,-1,104,0,104,0,99,0,1,0,0,0,0,0,0,255,17,17,1,1,19,109,3,22101,0,-2,1,21201,-1,0,2,21102,1,0,3,21101,414,0,0,1105,1,549,21201,-2,0,1,21202,-1,1,2,21101,429,0,0,1105,1,601,2101,0,1,435,1,386,0,386,104,-1,104,0,4,386,1001,387,-1,387,1005,387,451,99,109,-3,2106,0,0,109,8,22202,-7,-6,-3,22201,-3,-5,-3,21202,-4,64,-2,2207,-3,-2,381,1005,381,492,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,481,21202,-4,8,-2,2207,-3,-2,381,1005,381,518,21202,-2,-1,-1,22201,-3,-1,-3,2207,-3,-2,381,1006,381,507,2207,-3,-4,381,1005,381,540,21202,-4,-1,-1,22201,-3,-1,-3,2207,-3,-4,381,1006,381,529,22102,1,-3,-7,109,-8,2105,1,0,109,4,1202,-2,38,566,201,-3,566,566,101,639,566,566,1202,-1,1,0,204,-3,204,-2,204,-1,109,-4,2105,1,0,109,3,1202,-1,38,593,201,-2,593,593,101,639,593,593,21001,0,0,-2,109,-3,2105,1,0,109,3,22102,22,-2,1,22201,1,-1,1,21101,0,421,2,21102,594,1,3,21101,0,836,4,21101,630,0,0,1106,0,456,21201,1,1475,-2,109,-3,2105,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,2,0,2,0,0,2,0,0,0,2,2,0,2,2,2,0,2,0,0,2,0,2,2,0,0,0,0,0,2,0,2,2,0,0,0,1,1,0,2,0,0,2,0,0,0,2,0,0,0,2,0,2,0,2,0,2,0,2,2,2,0,2,0,2,0,0,2,0,2,2,0,0,0,1,1,0,2,2,0,2,0,2,2,0,0,0,2,2,0,2,0,0,0,0,2,2,0,2,2,2,0,2,2,0,2,0,2,2,0,0,0,1,1,0,2,2,2,2,2,2,0,2,2,2,2,0,0,2,2,0,0,2,2,2,2,2,0,0,0,0,2,2,2,2,2,2,2,0,0,1,1,0,2,2,0,2,0,2,2,2,2,2,2,0,0,2,2,2,2,2,2,0,0,2,0,0,0,2,2,2,2,0,2,0,0,0,0,1,1,0,2,0,0,0,2,0,2,0,2,2,2,0,0,2,2,0,0,2,2,2,0,0,0,0,0,2,2,2,0,0,2,0,2,0,0,1,1,0,2,2,0,0,2,2,2,0,0,0,0,0,2,0,0,2,2,2,2,0,2,0,0,2,0,0,2,2,0,0,0,0,2,2,0,1,1,0,0,0,2,0,2,0,2,0,2,2,0,2,2,2,0,2,2,0,2,2,0,0,0,2,0,0,0,2,2,2,0,0,0,0,0,1,1,0,0,0,2,0,0,2,2,0,2,0,2,0,2,0,0,2,0,2,0,0,0,2,2,2,2,2,2,0,2,2,2,2,2,2,0,1,1,0,0,2,0,2,2,2,0,0,2,0,2,0,2,2,2,0,0,2,2,0,2,0,2,2,2,2,2,2,2,0,2,0,2,0,0,1,1,0,2,0,2,0,0,0,0,0,0,0,0,0,2,2,2,2,0,0,0,0,0,2,0,2,2,0,2,0,2,2,2,2,2,2,0,1,1,0,2,2,0,0,0,2,2,2,0,0,2,2,0,2,0,2,2,0,2,2,2,0,0,2,2,0,2,2,0,0,2,2,2,2,0,1,1,0,0,2,0,0,2,0,0,0,0,0,0,2,2,0,2,2,2,0,0,0,0,0,0,0,2,0,0,2,0,0,2,2,0,2,0,1,1,0,2,0,0,2,2,2,0,2,2,2,2,0,0,2,2,0,2,0,2,2,2,2,2,2,2,0,2,2,2,2,2,2,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,64,86,97,12,60,6,31,61,53,79,45,82,7,4,9,5,60,42,15,39,54,90,43,57,68,25,79,48,37,54,2,55,31,6,48,97,78,53,17,72,15,58,88,20,60,98,39,43,49,7,32,59,11,32,67,3,96,42,4,6,34,58,24,37,15,87,72,83,76,30,89,70,86,55,42,15,62,21,65,88,35,52,79,16,20,94,18,98,68,58,83,25,72,39,92,66,41,50,92,25,90,17,86,53,89,64,12,54,98,97,49,31,43,59,33,55,58,11,27,62,30,23,20,4,24,13,37,16,82,66,57,58,28,97,35,84,89,13,1,57,1,55,90,98,17,22,43,70,33,6,77,9,17,6,70,72,15,22,72,75,35,84,93,74,10,69,8,6,85,39,7,98,55,39,66,39,52,60,63,3,49,59,28,37,8,84,75,6,98,37,8,19,91,74,54,42,70,94,18,10,1,34,67,10,5,75,98,59,35,77,54,59,88,14,28,10,72,11,30,85,35,88,94,44,3,71,2,91,63,71,4,50,23,38,75,95,17,20,28,88,34,30,93,79,63,61,75,40,75,47,72,25,15,49,62,64,91,72,5,36,90,45,52,80,48,19,70,45,7,72,44,5,39,11,27,32,97,98,73,51,33,56,9,54,33,36,4,10,84,82,20,28,9,41,26,78,96,5,61,20,44,70,59,69,59,48,24,91,88,46,2,67,14,89,44,82,40,25,53,91,11,61,55,88,95,55,92,9,81,76,59,76,94,2,34,3,57,61,11,87,18,23,77,94,72,88,1,95,77,64,3,77,2,6,42,52,79,27,69,59,33,36,20,44,6,45,36,9,10,51,12,64,11,62,83,36,50,61,85,20,16,81,36,94,54,17,72,28,26,53,47,42,38,72,87,59,17,63,8,12,48,22,77,45,42,33,6,29,87,53,66,35,32,32,24,72,31,96,17,83,62,1,66,54,96,1,37,74,53,26,55,9,22,69,66,46,40,97,9,85,10,51,38,70,44,5,59,59,87,25,90,73,11,74,63,33,33,25,65,69,80,20,30,32,10,86,29,18,67,77,76,89,9,55,89,70,95,49,38,89,58,45,52,44,35,66,19,48,82,67,60,92,66,38,21,54,6,6,86,29,45,2,24,13,35,51,20,5,61,1,47,88,50,45,78,80,46,81,17,26,7,34,28,41,14,15,79,23,8,57,69,58,92,66,92,70,59,40,74,28,21,33,77,27,95,93,67,7,14,68,29,44,98,14,51,25,64,10,60,67,9,6,69,25,41,78,81,32,35,96,89,29,69,35,93,61,25,35,71,61,97,40,67,36,29,77,42,34,31,59,47,63,22,19,39,6,42,33,79,4,76,38,75,5,1,29,31,38,3,64,35,33,19,90,43,47,30,43,86,33,76,4,85,66,26,98,91,33,59,93,6,78,27,31,22,89,78,86,70,49,83,81,15,20,8,2,13,30,18,22,73,53,37,48,66,93,46,27,62,72,55,65,9,83,20,32,41,12,63,20,16,55,98,31,20,46,27,17,93,84,59,15,90,29,72,13,83,88,21,49,29,67,47,7,7,12,38,36,25,16,20,80,63,55,46,27,51,72,79,94,68,75,34,41,24,91,72,64,90,81,82,93,96,47,1,57,75,81,56,14,57,58,54,24,40,40,71,46,16,3,34,79,46,28,42,9,55,87,85,23,14,11,98,15,31,28,44,81,96,94,10,51,44,57,11,55,31,15,9,93,76,92,69,12,25,27,82,43,80,54,18,58,6,82,59,81,65,96,38,69,2,28,86,70,22,66,10,5,88,56,79,31,77,48,61,34,87,7,17,21,37,16,26,68,64,72,30,3,6,88,26,24,3,77,50,34,67,79,31,3,77,26,72,51,23,25,194223"""


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


def run_program(program_input, input_val=None, opcode_idx=0, out=None, relative_base=0):
    program = list(program_input)
    while opcode_idx < len(program):
        opcode_raw = program[opcode_idx]
        opcode, param1_mode, param2_mode, param3_mode = parse_opcode(opcode_raw)
        # print(
        #     f"opcode at {opcode_idx}: {(opcode, param1_mode, param2_mode, param3_mode)}"
        # )
        # print_program(program)

        if opcode == 99:
            print("halt", out)
            break

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
            if input_val is None:
                print("wait input")
                input_val = yield
                print("got input", input_val)
                yield None

            res_idx = get_res_idx(program, opcode_idx + 1, param1_mode, relative_base)

            print("use input", input_val)
            write(program, res_idx, input_val)

            input_val = None

            opcode_idx += 2
        # output
        elif opcode == 4:
            out = get_param(program, opcode_idx + 1, param1_mode, relative_base)
            opcode_idx += 2

            print("out", out)
            yield out

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


TILES = {
    0: " ",  # empty
    1: "#",  # wall
    2: ".",  # block
    3: "=",  # paddle
    4: "o",  # ball
}


def run():
    program = run_program(INPUT)
    output = []
    for out in program:
        if out is None:
            print("input required")
            break
        else:
            output.append(out)
    screen = {}
    for idx in range(0, len(output), 3):
        x, y, t = output[idx : idx + 3]
        screen[(x, y)] = t

    print(sum(1 for p, t in screen.items() if t == 2))


if __name__ == "__main__":
    run()
