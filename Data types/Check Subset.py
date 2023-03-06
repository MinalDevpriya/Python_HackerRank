#https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())

for _ in range(a):
    n1 = int(input())
    s1 = set(map(int, input().split()))
    n2 = int(input())
    s2 = set(map(int, input().split()))

    print(s1.issubset(s2))

