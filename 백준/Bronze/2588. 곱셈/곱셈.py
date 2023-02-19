import sys

#sys = open("input.txt", "rt")
a = int(sys.stdin.readline())
b = sys.stdin.readline()

for i in reversed(range(3)):
    print(a * int(b[i]))

print(a * int(b))