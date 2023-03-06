#https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m=list(map(int, input().split()))
arr, a, b=list(map(int,input().split())), set(map(int, input().split())), set(map(int, input().split()))

x=set(arr) & a
y=set(arr) & b
c=0
for i in arr:
    if i in x:
        c+=1
    elif i in y:
        c-=1
print(c)