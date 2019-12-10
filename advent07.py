def run():
    count = 0
    for x in range(347312, 805916):
        x = list(str(x))
        double_found = False
        for d1, d2 in zip(x[1:], x):
            if d1 < d2:
                break
            if d1 == d2:
                double_found = True
        else:
            if double_found:
                count += 1
    return count


if __name__ == "__main__":
    print(run())
