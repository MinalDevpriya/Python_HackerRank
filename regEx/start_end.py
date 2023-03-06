#https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true
import re

s, k = input(), input()
p = re.compile(k)
m = p.search(s)

if not m:
    print((-1, -1))

while m:
    print((m.start(), m.end() - 1))
    m = p.search(s, m.start() + 1)