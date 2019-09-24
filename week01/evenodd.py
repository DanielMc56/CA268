import sys

f = sys.argv[1]

if len(f) % 2 == 0:
   print(f[len(f) // 2:])
else:
   print(f[0] + f[-1])
