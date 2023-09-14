if __name__ == '__main__':
    college = []
    for _ in range(int(input())):
        student = []
        name = input()
        score = float(input())
        student.append(name)
        student.append(score)
        college.append(student)

    # sort by second element of tuple, i.e. score
    college.sort(key=lambda x: (x[1]))
    # reconstruct list if lowest score not present, i.e. remove lowest score
    college2 = [[item[0], item[1]]
                for item in college if item[1] != (college[0][1])]
    # reconstruct list of only names if score == lowest in college2
    college3 = [item[0] for item in college2 if item[1] == (college2[0][1])]
    college3.sort()  # sort names
    for w in college3:
        print(w)
