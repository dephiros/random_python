def check_braces(expressions):
  # Write your code here
  # To print results to the standard output you can use print
  # Example print "Hello world!"
  lefts = "([{"
  rights = ")]}"
  result = 0
  for e in expressions:
    stack = []
    i = 0
    for i, s in enumerate(e):
      if s in rights:
        if len(stack) == 0 or stack[-1] != lefts[rights.index(s)]:  # no matching bracket for right
          break
        else:
          stack.pop()
      else:
        stack.append(s)
    if len(stack) == 0 and i == len(e) - 1:  # all bracket is matched
      print 1
    else:
      print 0

# check_braces([ ")(){}", "[]({})", "([])", "{()[]}", "([)]" ])__author__ = 'annguyen'
