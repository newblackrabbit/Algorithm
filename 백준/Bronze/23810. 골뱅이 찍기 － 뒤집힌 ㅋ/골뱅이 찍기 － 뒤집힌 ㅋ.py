import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    print('@'*n*5)
for i in range(n):
    print('@'*n)
for i in range(n):
    print('@'*n*5)
for i in range(2*n):
    print('@'*n)
