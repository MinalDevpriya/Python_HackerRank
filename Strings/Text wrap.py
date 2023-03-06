#https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
def wrap(string, max_width):
    s=textwrap.fill(string, max_width)
    return s