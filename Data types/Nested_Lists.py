#https://www.hackerrank.com/challenges/nested-list/problem?isFullScre
# en=true
if __name__ == '__main__':
    scorel = []
    l1 = []
    l2 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l1.append([name, score])
        scorel.append(score)

    scoresl = list(set(scorel))
    scoresl.sort()
    slowest = scoresl[1]
    for i in range(len(l1)):
        if l1[i][1] == slowest:
            l2.append(l1[i][0])
        l2.sort()
    for j in range(len(l2)):
        print(l2[j])
