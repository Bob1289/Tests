

def sol1(scores):
    scores.sort()
    return scores[-1]

def sol2(scores):
    highest = 0

    for i in range(len(scores)):
        if scores[i] < scores[i - 1]:
            highest = scores[i - 1]
    return highest


def sol3(scores):
    highest = 0

    for i in scores:
        if i > highest:
            highest = i
    return highest
        
def sol4(scores):
    return max(scores)


if __name__ == '__main__':
    student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

    print(sol1(student_scores))
    print(sol2(student_scores))
    print(sol3(student_scores))
    print(sol4(student_scores))