#https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem?isFullScreen=true
import re
[print(\
re.sub(r'(?<= )\|\|(?= )', "or", (\
re.sub(r'(?<= )\&\&(?= )', "and", \
input())))) \
for _ in range(int(input()))\
]