#https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
def swap_case(s):
    c=""
    for i in range (len(s)):
        if (s[i]==s[i].upper()):
            c+=s[i].lower()
        elif (s[i]==s[i].lower()):
            c+=s[i].upper()
        else:
            c+=c
    return c
