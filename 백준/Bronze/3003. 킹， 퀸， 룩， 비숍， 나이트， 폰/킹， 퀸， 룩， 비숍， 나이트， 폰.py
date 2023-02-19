import sys

#sys = open("input.txt", "rt")
chess_Basic = [1, 1, 2, 2, 2, 8]
data = list(map(int, sys.stdin.readline().split()))
for i in range(0, len(data)):
    print(chess_Basic[i] - data[i], end=" ")