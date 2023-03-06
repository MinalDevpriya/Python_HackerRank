#https://www.hackerrank.com/challenges/introduction-to-regex/problem
import re

f = re.compile("[+-]?[0-9]*\.[0-9]+")


def float_check(s):
    if f.fullmatch(s):
        return True
    else:
        return False


i = int(input())
for i in range(i):
    print(float_check(input()))