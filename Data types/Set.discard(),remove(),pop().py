#https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true
n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    name, *args=input().split()
    getattr(s, name)(*map(int, args))
print(sum(s))
