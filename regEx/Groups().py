#https://www.hackerrank.com/challenges/re-group-groups/problem?isFullScreen=true
import re
m=re.search(r"([a-z0-9])\1{1,}", input())

if m:
    print(m.group(1))
else:
    print(-1)