__author__ = 'annguyen'


def find_deviation(v, d):
  # Write your code here
  # To print results to the standard output you can use print
  # Example print "Hello world!"
  max_med = 0
  current_max = 0
  current_min = float('inf')
  for i in xrange(0, len(v) - d + 1):
    # print v[i + d - 1], current_max, current_min
    if v[i + d - 1] > current_max or v[i + d - 1] < current_min:
      r = v[i: i + d]
      mx = max(r)
      mn = min(r)
      med = mx - mn
      current_max = mx if mx > current_max else current_max
      current_min = mn if mn < current_min else current_min
      max_med = med if med > max_med else med
  print max_med


find_deviation([6, 9, 4, 7, 4, 1], 3)
