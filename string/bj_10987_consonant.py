import sys
print(sum([1 if c in ['a','e','i','o','u'] else 0 for c in sys.stdin.readline()]))
