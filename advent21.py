from collections import deque, OrderedDict

INPUT = "3,8,1005,8,311,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,28,2,103,7,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,55,2,3,6,10,1,101,5,10,1,6,7,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,89,1,1108,11,10,2,1002,13,10,1006,0,92,1,2,13,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,126,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,147,1,7,0,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,173,1006,0,96,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,1001,8,0,198,1,3,7,10,1006,0,94,2,1003,20,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,232,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,253,1006,0,63,1,109,16,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,101,0,8,283,2,1107,14,10,1,105,11,10,101,1,9,9,1007,9,1098,10,1005,10,15,99,109,633,104,0,104,1,21102,837951005592,1,1,21101,328,0,0,1105,1,432,21101,0,847069840276,1,21101,0,339,0,1106,0,432,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,179318123543,1,1,21102,386,1,0,1106,0,432,21102,1,29220688067,1,21102,1,397,0,1106,0,432,3,10,104,0,104,0,3,10,104,0,104,0,21102,709580567396,1,1,21102,1,420,0,1105,1,432,21102,1,868498694912,1,21102,431,1,0,1106,0,432,99,109,2,22101,0,-1,1,21101,40,0,2,21101,0,463,3,21101,0,453,0,1105,1,496,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,458,459,474,4,0,1001,458,1,458,108,4,458,10,1006,10,490,1102,1,0,458,109,-2,2105,1,0,0,109,4,1202,-1,1,495,1207,-3,0,10,1006,10,513,21102,0,1,-3,21201,-3,0,1,21202,-2,1,2,21101,0,1,3,21101,0,532,0,1106,0,537,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,560,2207,-4,-2,10,1006,10,560,22102,1,-4,-4,1105,1,628,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21101,0,579,0,1105,1,537,22101,0,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,598,21102,1,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,620,22102,1,-1,1,21101,0,620,0,106,0,495,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0"

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


def get_dir(dir_state, cmd):
    # 0 - left 90 degrees
    # 1 - right 90 degrees
    if cmd == 0:
        dir_state.rotate(1)
    else:
        dir_state.rotate(-1)
    return dir_state[0]


def get_next_point(cur_point, cur_dir):
    x, y = cur_point
    if cur_dir == "up":
        return x, y + 1
    elif cur_dir == "right":
        return x + 1, y
    elif cur_dir == "down":
        return x, y - 1
    else:
        return x - 1, y


COLORS = {0: ".", 1: "#"}
COLORS_INV = {v: k for k, v in COLORS.items()}


def eval_robot_program(robot_program, points, cur_point, dir_state):
    print("start eval", robot_program)
    for idx in range(0, len(robot_program), 2):
        color_idx, dir_cmd = robot_program[idx : idx + 2]
        color = COLORS[color_idx]
        points[cur_point] = color
        print(color_idx, dir_cmd, (cur_point, color))
        cur_dir = get_dir(dir_state, dir_cmd)
        cur_point = get_next_point(cur_point, cur_dir)
        input_val = COLORS_INV[points.get(cur_point, ".")]

    return points, cur_point, dir_state, input_val


def run():
    points = OrderedDict()

    cur_point = (0, 0)
    dir_state = deque(["up", "right", "down", "left"])
    color_idx = 0
    input_val = color_idx
    program = run_program(INPUT, input_val=input_val)
    robot_program = []
    for out in program:
        # print("process out", out)
        if out is None:
            points, cur_point, dir_state, input_val = eval_robot_program(
                robot_program, points, cur_point, dir_state
            )
            program.send(input_val)
            robot_program.clear()
        else:
            robot_program.append(out)
            # print("collected", robot_program)

    if robot_program:
        points, cur_point, dir_state, input_val = eval_robot_program(
            robot_program, points, cur_point, dir_state
        )

    painted_panels_count = len(set(points))
    print(painted_panels_count)


if __name__ == "__main__":
    run()
