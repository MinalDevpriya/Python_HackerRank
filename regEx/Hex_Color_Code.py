#https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true
import re
n=int(input())
text='\n'.join([input() for _ in range(n)])
pattern=re.compile(r'(?<=.)#[0-9a-fA-F]{3,6}')
matches=pattern.findall(text)
[print(match) for match in matches]