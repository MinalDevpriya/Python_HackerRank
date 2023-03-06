#https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
M=set(map(int, input().split()))
b=int(input())
N=set(map(int, input().split()))

output=sorted(list(M.union(N).difference(M.intersection(N))))
for i in output:
    print(i)
