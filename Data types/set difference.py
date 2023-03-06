#https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
a=input()
s=set(input().split())
b=input()
print(len(s.difference(input().split())))
