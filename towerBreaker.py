def towerBreakers(n, m):
    if n % 2 == 0:
        return 2
    else:
        return 1 if m > 2 else 2