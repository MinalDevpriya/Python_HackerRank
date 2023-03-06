#https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    li=student_marks[query_name]
    result=0
    for i in range(len(li)):
        result=result+li[i]
    print("%.2f"% (result/len(li)))