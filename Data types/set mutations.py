#https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
s=set(map(int, input().split()))

for _ in range(int(input())):
    name, *_=input().split()
    getattr(s,name)(set(map(int, input().split())))
print(sum(s))