#https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
a=input()
s1=set(map(int,input().split()))
b=input()
s2=set(map(int,input().split()))
print(len(s1.symmetric_difference(s2)))