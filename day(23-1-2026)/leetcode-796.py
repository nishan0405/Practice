def hurdleRace(k, height):
    # Write your code here
    maximum=max(height)
    if maximum<=k:
        return 0
    else:
        n=maximum-k
        return n