def four_letters(names):
    arr = names.split()
    cnt = 0

    for i in arr:
        if len(i) == 4:
            cnt += 1

    return cnt