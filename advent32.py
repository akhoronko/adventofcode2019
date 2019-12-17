from itertools import cycle, chain, repeat, islice

INPUT = """59719811742386712072322509550573967421647565332667367184388997335292349852954113343804787102604664096288440135472284308373326245877593956199225516071210882728614292871131765110416999817460140955856338830118060988497097324334962543389288979535054141495171461720836525090700092901849537843081841755954360811618153200442803197286399570023355821961989595705705045742262477597293974158696594795118783767300148414702347570064139665680516053143032825288231685962359393267461932384683218413483205671636464298057303588424278653449749781937014234119757220011471950196190313903906218080178644004164122665292870495547666700781057929319060171363468213087408071790"""

INPUT = tuple(map(int, INPUT.strip()))


def run(n=100):
    # input = main_input * 10000
    # offset = int(input[:7])
    # input = [int(x) for x in input]
    # input_length = int(len(input))
    #
    # last_output = input.copy()
    # for i in range(100):
    #     new_output = last_output.copy()
    #     for j in reversed(range(offset, input_length)):
    #         new_val = (last_output[j - 1] + new_output[j]) % 10
    #         new_output[j - 1] = new_val
    #     last_output = new_output.copy()
    #
    # result_str = ''.join(map(str, last_output[offset:offset + 8]))

    offset = int("".join(map(str, INPUT[:7])))
    print("offset", offset)
    full_input_len = len(INPUT) * 10000

    inp = list(islice(cycle(INPUT), offset, full_input_len))
    print("tail", len(inp))

    for phase in range(1, n + 1):
        out = inp.copy()

        for idx in range(len(inp)-1, -1, -1):
            val = (inp[idx - 1] + out[idx]) % 10
            out[idx - 1] = val

        inp = out

    print("".join(map(str, inp[:8])))


if __name__ == "__main__":
    run()