
number_of_questions, number_of_students = tuple(map(int, input().split()))
student_comfort = list(map(int, input().split()))

student_comfort.sort()

for _ in range(number_of_questions):

    question_difficulty = int(input())
    left = -1
    right = number_of_students
    
    # binary search
    while right > left + 1:
        mid = left + (right - left)//2

        if student_comfort[mid] < question_difficulty:
            left = mid
        else:
            right = mid
    
    is_good = (left > -1) and ((number_of_students - right)*2 > number_of_students)
    print("YES" if is_good else "NO")


