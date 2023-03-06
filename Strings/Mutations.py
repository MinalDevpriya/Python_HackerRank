#https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
def mutate_string(string, position, character):
    res=string[:position]+character+string[position+1:]
    return res
