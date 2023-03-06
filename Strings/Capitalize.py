#https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
# Complete the solve function below.
def solve(s):
    w=""
    for i in range(len(s)):
        if i==0:
            w=w+(s[i].upper())
        elif(s[i-1]==" "):
            w=w+(s[i].upper())
        else:
            w=w+s[i]
    return w
