def get_total_time(heroes, n):
    if len(heroes) <= n:
        return max(heroes)

    cache = []

    for i in range(n):
        cache.append(heroes[i])
    cache = sorted(cache, reverse=True)

    for i in range(n, len(heroes)):
        cache.append(cache.pop() + heroes[i])
        cache = sorted(cache, reverse=True)

    ans = 0
    while len(cache) > 0:
        ans = cache.pop()

    return ans