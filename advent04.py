INPUT = (
    1,
    0,
    0,
    3,
    1,
    1,
    2,
    3,
    1,
    3,
    4,
    3,
    1,
    5,
    0,
    3,
    2,
    13,
    1,
    19,
    1,
    5,
    19,
    23,
    2,
    10,
    23,
    27,
    1,
    27,
    5,
    31,
    2,
    9,
    31,
    35,
    1,
    35,
    5,
    39,
    2,
    6,
    39,
    43,
    1,
    43,
    5,
    47,
    2,
    47,
    10,
    51,
    2,
    51,
    6,
    55,
    1,
    5,
    55,
    59,
    2,
    10,
    59,
    63,
    1,
    63,
    6,
    67,
    2,
    67,
    6,
    71,
    1,
    71,
    5,
    75,
    1,
    13,
    75,
    79,
    1,
    6,
    79,
    83,
    2,
    83,
    13,
    87,
    1,
    87,
    6,
    91,
    1,
    10,
    91,
    95,
    1,
    95,
    9,
    99,
    2,
    99,
    13,
    103,
    1,
    103,
    6,
    107,
    2,
    107,
    6,
    111,
    1,
    111,
    2,
    115,
    1,
    115,
    13,
    0,
    99,
    2,
    0,
    14,
    0,
)


def reset_1202_program_alarm(noun, verb):
    program = list(INPUT)
    program[1] = noun
    program[2] = verb
    return program


def run(noun, verb):
    program = reset_1202_program_alarm(noun, verb)
    opcode_idx = 0
    while opcode_idx < len(program):
        # print_program(program)
        opcode = program[opcode_idx]
        # print(f"opcode at {opcode_idx}: {opcode}")

        if opcode == 99:
            # print("halt")
            break

        arg1 = program[program[opcode_idx + 1]]
        arg2 = program[program[opcode_idx + 2]]
        res_idx = program[opcode_idx + 3]

        if opcode == 1:
            program[res_idx] = arg1 + arg2
        elif opcode == 2:
            program[res_idx] = arg1 * arg2
        else:
            print(f"bad opcode {opcode} at idx {opcode_idx}: {program}")
            break

        # op = "+" if opcode == 1 else "*"
        # print(
        #     f"p[{res_idx}] = p[{opcode_idx + 1}] {op} p[{opcode_idx + 2}] = "
        #     f"{arg1} {op} {arg2} = {program[res_idx]}"
        # )

        opcode_idx += 4

    return program[0]


def print_program(p, step=4):
    for idx in range(0, len(p), step):
        line = ", ".join(map(str, p[idx:idx+step]))
        print(f"[{idx} : {idx+step-1}]: {line}")


def find_noun_verb(res=19690720):
    for noun in range(0, 100):
        for verb in range(0, 100):
            out = run(noun, verb)
            print(f"{(noun, verb)} -> {out}")
            if out == res:
                return noun, verb


if __name__ == "__main__":
    noun, verb = find_noun_verb()
    print(noun, verb)
    print(100 * noun + verb)

