def fib(n):
  """
  Generator for Fibonacci serie

  Each call to fib() returns the next value in the serie
  Example: for i in fib(5): print i
  @param n fib range upper bound
  """
  a, b = 0, 1
  i = 0
  while i < n:
    yield b
    a, b = b, a+b
    i += 1

