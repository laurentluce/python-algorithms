def permutations(lst):
    """Generator for list permutations.

    @param lst list to generate permutations for
    @result yield each permutation

    Example:
    lst = [1,2,3]
    a = [1]
    permutations([2,3]) = [[2,3], [3,2]]
    [2,3]
    yield [1,2,3]
    yield [2,1,3]
    yield [2,3,1]
    [3,2]
    yield [1,3,2]
    yield [3,1,2]
    yield [3,2,1]
    """
    if len(lst) <= 1:
        yield lst
    else:
        a = [lst.pop(0)]
        for p in permutations(lst):
            for i in range(len(p)+1):
                yield p[:i] + a + p[i:]
