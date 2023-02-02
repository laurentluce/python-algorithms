def find_int(i, lst):
    """Find integer in a sorted list.

    Example: 4 in [1, 3, 4, 6, 7, 9] -> 2
    @param i integer to find.
    @param lst sorted list.
    @returns index if found, None if not.
    """
    if lst:
        p_idx = len(lst) / 2
        p = lst[p_idx]
        if i == p:
            return p_idx
        elif len(lst) == 1:
            return
        elif i < p:
            res = find_int(i, lst[:p_idx])
            if res:
                return res
        elif i > p:
            res = find_int(i, lst[p_idx:])
            if res:
                return res + p_idx


def find_max_sub(lst):
    """Find subset with highest sum.

    Example: [-2, 3, -4, 5, 1, -5] -> (3,4), 6
    @param lst list
    @returns subset bounds and highest sum
    """
    # max sum
    max = lst[0]
    # current sum
    m = 0
    # max sum subset bounds
    bounds = (0, 0)
    # current subset start
    s = 0
    for i in range(len(lst)):
        m += lst[i]
        if m > max:
            max = m
            bounds = (s, i)
        elif m < 0:
            m = 0
            s = i+1
    return bounds, max


def merge_sort(lst):
    """Sort list using merge sort.

    Complexity: O(n log n)

    @param l list to sort.
    @returns sorted list.
    """
    def merge(l1, l2):
        """Merge sorted lists l1 and l2.

        [1, 2, 4], [1, 3, 4, 5] -> [1, 1, 2, 3, 4, 5]
        @param l1 sorted list
        @param l2 sorted list
        @returns merge sorted list
        """
        res = []
        i = 0
        j = 0
        while i < len(l1) and j < len(l2):
            if l1[i] <= l2[j]:
                res.append(l1[i])
                i += 1
            elif l2[j] < l1[i]:
                res.append(l2[j])
                j += 1

        while i < len(l1):
            res.append(l1[i])
            i += 1

        while j < len(l2):
            res.append(l2[j])
            j += 1

        return res

    length = len(lst)
    if length <= 1:
        return lst
    mid = length / 2
    h1 = merge_sort(lst[:mid])
    h2 = merge_sort(lst[mid:])

    return merge(h1, h2)


def quicksort(lst):
    """Sort list using quick sort.

    Complexity: O(n log n).  Worst: O(n2)

    @param lst list to sort.
    @returns sorted list.
    """
    if len(lst) <= 1:
        return lst

    pivot = lst[0]
    less = []
    equal = []
    greater = []
    for e in lst:
        if e < pivot:
            less.append(e)
        elif e == pivot:
            equal.append(e)
        else:
            greater.append(e)

    return quicksort(less) + equal + quicksort(greater)
