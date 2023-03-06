#https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=tru
if __name__ == '__main__':
    s = input()
    aln = 0
    alp = 0
    dg = 0
    low = 0
    up = 0
    for ch in s:
        if ch.isalnum():
            aln += 1
        if ch.isalpha():
            alp += 1
        if ch.isdigit():
            dg += 1
        if ch.islower():
            low += 1
        if ch.isupper():
            up += 1

    if aln >= 1:
        print(True)
    else:
        print(False)
    if alp >= 1:
        print(True)
    else:
        print(False)
    if dg >= 1:
        print(True)
    else:
        print(False)
    if low >= 1:
        print(True)
    else:
        print(False)
    if up >= 1:
        print(True)
    else:
        print(False)