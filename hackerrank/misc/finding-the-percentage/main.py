if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # write your code here:
    score = student_marks[query_name]
    mean_score = sum(score)/(len(score))
    print(f"{mean_score:.2f}")
