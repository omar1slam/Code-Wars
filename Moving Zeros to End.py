# Move zeros to the end of list
# https://www.codewars.com/kata/52597aa56021e91c93000cb0
# 5 kyu
import timeit as time

def move_zeros(a):
    i = 0
    counter = 0
    while i < len(a) and counter < len(a):
        if (a[i] == 0) and (a[i] is not False):
            a.append(0)
            a.pop(i)
            counter +=1
        else:
            counter = 0
            i+=1
    return a

print(move_zeros(['a', 0, 'b', 'c', 'd', 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0]))
##########################################DONE#########################################

