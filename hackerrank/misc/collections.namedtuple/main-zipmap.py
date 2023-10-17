# Enter your code here. Read input from STDIN. Print output to STDOUT

from statistics import mean

n = int(input())
headers = input().split()

score = []
for rec in range(n):
    rec = input().split()
    student = dict(zip(headers, rec))
    score.append(int(student['MARKS']))
ave_score = "{:.2f}".format(mean(score))
print(ave_score)
