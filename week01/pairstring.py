import sys

f = sys.argv[1]

i = 1
while i < len(f):
   print(f[i - 1] + f[i])
   i += 1
