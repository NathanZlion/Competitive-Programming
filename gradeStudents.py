#!/bin/python3

import math
import os
import random
import re
import sys


def gradingStudents(grades):
    def round(num):
        roundup = num
        while roundup % 5 != 0:
            roundup += 1
        if roundup - num <= 2:
            return roundup
        return num
    
    finalGrades = []
    for grade in grades:
        if grade%5 == 0 or grade <= 38:
            finalGrades.append(grade)
        else:
            finalGrades.append(round(grade))            
    return finalGrades            

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
