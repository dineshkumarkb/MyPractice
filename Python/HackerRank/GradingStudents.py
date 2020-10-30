#!/bin/python

from __future__ import print_function

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    for i in range(len(grades)):
        if (abs((grades[i]//5 + 1) * 5) - grades[i] < 3):
            if(grades[i] >= 38):
                grades[i] = ((grades[i]//5 + 1) * 5)

    return grades





if __name__ == '__main__':

    n = int(raw_input())

    grades = []

    for _ in xrange(n):
        grades_item = int(raw_input())
        grades.append(grades_item)

    result = gradingStudents(grades)
