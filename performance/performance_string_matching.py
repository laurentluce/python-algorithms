import time
import string_matching

class StringMatchingPerformance:
   
  def __init__(self):
    pass

  def calculate_performance(self):
    t = 'ababbababa'
    s = 'aba'
    times = 1000
    
    ts = time.time()
    for i in range(times):
      string_matching.string_matching_naive(t, s)
    t1 = time.time() - ts
    print 'string_matching_naive: %.2f seconds' % t1

    ts = time.time()
    for i in range(times):
      string_matching.string_matching_rabin_karp(t, s)
    t2 = time.time() - ts
    print 'string_matching_rabin_karp: %.2f seconds' % t2

    ts = time.time()
    for i in range(times):
      string_matching.string_matching_knuth_morris_pratt(t, s)
    t2 = time.time() - ts
    print 'string_matching_knuth_morris_pratt: %.2f seconds' % t2

    ts = time.time()
    for i in range(times):
      string_matching.string_matching_boyer_moore_horspool(t, s)
    t2 = time.time() - ts
    print 'string_matching_boyer_moore_horspool: %.2f seconds' % t2

if __name__ == '__main__':
  p = StringMatchingPerformance()
  p.calculate_performance()

