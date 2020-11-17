def broken_device(x, y):
    if x == y:
        return 0

    if x > y:
        return x - y

    if y % 2 == 1:
        return 1 + broken_device(x, y + 1)
    else:
        return 1 + broken_device(x, y / 2)
