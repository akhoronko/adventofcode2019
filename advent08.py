from collections import Counter


def run():
    count = 0
    for x in range(347312, 805916):
        x = list(str(x))
        for d1, d2 in zip(x[1:], x):
            if d1 < d2:
                break
        else:
            digits = Counter(x)
            if any(v == 2 for v in digits.values()):
                count += 1

    return count


if __name__ == "__main__":
    print(run())
