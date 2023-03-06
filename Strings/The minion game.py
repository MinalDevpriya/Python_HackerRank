#https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
def minion_game(string):
    # your code goes here
    s, k = 0, 0
    vowels = 'AEIOU'
    n = len(string)
    for i in range(n):
        if string[i] in vowels:
            k = k + (len(string) - i)
        else:
            s = s + (len(string) - i)

    if s == k:
        print('Draw')
    elif s > k:
        print(f'Stuart {s}')
    else:
        print(f'Kevin {k}')

