# Enter your code here. Read input from STDIN. Print output to STDOUT

k = int(input())
rooms = input().split()

room_score = {}

for item in rooms:
    if item not in room_score.keys():
        room_score[item] = 1
    else:
        room_score[item] += 1
# get key by value
print(list(room_score.keys())[list(room_score.values()).index(1)])
