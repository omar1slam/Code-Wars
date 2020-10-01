# Find multiples of 3 and 5 below the number given
# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
# 6 kyu

def solution(number):
    found = []
    for i in range(number-1,0,-1):
        if (i % 3) == 0 or (i % 5) == 0:
            if i not in found:
                found.append(i)

    return sum(int(digit) for digit in found)


#############################DONE#####################





