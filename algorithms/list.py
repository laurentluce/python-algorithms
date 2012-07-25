def find_max_sub(l):
    """
    Find subset with higest sum

    Example: [-2, 3, -4, 5, 1, -5] -> (3,4), 6
    @param l list
    @returns subset bounds and highest sum
    """
    # max sum
    max = l[0]
    # current sum
    m = 0
    # max sum subset bounds
    bounds = (0, 0)
    # current subset start
    s = 0
    for i in range(len(l)):
        m += l[i]
        if m > max:
            max = m
            bounds = (s, i)
        elif m < 0:
            m = 0
            s = i+1
    return bounds, max
