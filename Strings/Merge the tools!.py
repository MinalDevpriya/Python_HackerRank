#https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
from textwrap import wrap

def merge_the_tools(string, k):
    # your code goes here
    ls=wrap(string,k)
    for x in ls:
        result=x[0]
        for i in range(1,k):
            if x[i] not in result:
                result +=x[i]
            else:
                continue
        print(result)