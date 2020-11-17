def get_number_of_boats(dwarfs, limit):
    dwarfs = sorted(dwarfs)
    ans = len(dwarfs)

    i = 0
    j = ans - 1

    while i < j:
        if dwarfs[i] + dwarfs[j] <= limit:
            ans -= 1
            i += 1
        j -= 1

    return ans
