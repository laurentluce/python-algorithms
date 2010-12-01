def permutations(l):
  """
  Generator for list permutations
  
  Example: [1,2,3] = [1,2,3], [1,3,2], [2,1,3] ...

  @param l list to generate permutations for
  @result yield each permutation
  """
  print 'permutations: ',l
  if len(l) <= 1:
    yield l
  else:
    a = [l.pop(0)]
    for p in permutations(l):
      for i in range(len(p)+1):
        yield p[:i] + a + p[i:]

