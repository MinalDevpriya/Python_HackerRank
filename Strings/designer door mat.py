#https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int, input().split())
#top
for i in range (n):
    if i%2==1:
        print((".|."*i).center(m,"-"))
#middle
print("WELCOME".center(m,"-"))

#bottom
for i in range(1,n):
    if (n-i)%2==1:
        print((".|."*(n-i)).center(m,"-"))
