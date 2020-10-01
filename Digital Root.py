# Find sum of all digits in a number
# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
# 6 kyu


def digital_root(n):
    a = str(n)
    b = 0
    if len(a) == 1:
        return n
    else:
        for i in range(len(a)):
            b += int(a[i])
        return digital_root(b)


print(digital_root(132189))


#########################DONE##########################################