import sys
a, b = map(int, sys.stdin.readline().split())
c = int(input())

time = a * 60 + b + c
a = time // 60 
b = time % 60

if a >= 24:
    a -= 24

print (a, b)