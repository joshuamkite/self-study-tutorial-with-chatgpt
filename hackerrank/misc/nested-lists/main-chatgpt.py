if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])  # Append as a list

    # Sort by score
    students.sort(key=lambda x: x[1])

    # Find the second lowest score
    second_lowest_score = next(
        student[1] for student in students if student[1] != students[0][1])

    # Filter names with the second lowest score and sort them
    second_lowest_names = sorted(
        [student[0] for student in students if student[1] == second_lowest_score])

    # Print the names
    for name in second_lowest_names:
        print(name)
