def hurdleRace(k, height):
    if max(height)<=k:
        return 0
    return (abs(max(height)-k))