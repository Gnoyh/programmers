# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    students_count = [0] * 4
    students_answers = [[], [1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    
    for i in range(1, 4):
        student_answers = students_answers[i] * (len(answers) // len(students_answers[i]) + 1)
        
        for j in range(len(answers)):
            if answers[j] == student_answers[j]:
                students_count[i] += 1
                
    return [i for i in range(1, 4) if students_count[i] == max(students_count)]