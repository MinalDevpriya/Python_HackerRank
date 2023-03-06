#https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

a=int(input())
print(Counter(input().split()).most_common()[-1][0])
