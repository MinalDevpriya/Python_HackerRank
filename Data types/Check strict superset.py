#https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT

s1=set(input().split())
result=True
for _ in range(int(input())):
    t=set(input().split())
    if not s1.issuperset(t):
        result=False
        break
print(result)