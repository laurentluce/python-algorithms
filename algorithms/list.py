def find_int(i, l):
    """
    Find integer in a sorted list.

    Example: 4 in [1, 3, 4, 6, 7, 9] -> 2
    @param i integer to find.
    @param l sorted list.
    @returns index if found, None if not.
    """
    if l:
        p_idx = len(l) / 2
        p = l[p_idx]
        if i == p:
            return p_idx
        elif len(l) == 1:
            return
        elif i < p:
            res = find_int(i, l[:p_idx])
            if res:
                return res
        elif i > p:
            res = find_int(i, l[p_idx:])
            if res:
                return res + p_idx

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
