from collections import namedtuple
from statistics import mean

n = int(input())
headers = input().split()

# Define the named tuple based on the headers
Student = namedtuple('Student', headers)

scores = []
for _ in range(n):
    rec = input().split()
    student = Student(*rec)
    scores.append(int(student.MARKS))

ave_score = "{:.2f}".format(mean(scores))
print(ave_score)
