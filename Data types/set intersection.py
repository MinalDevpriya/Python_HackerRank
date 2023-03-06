#https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
set1=set(map(int, input().split()))
b=int(input())
set2=set(map(int, input().split()))
print(len(set1 & set2))