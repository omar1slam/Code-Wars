# Create Phone Number
# https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python
# 6 kyu
# First challenge!

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def create_phone_number(n):
    b = ''
    for i in range(len(n)):
        b += str(n[i])
    return "({}) {}-{}".format(b[0:3],b[3:6], b[6:10])


print(create_phone_number(a))


#########################DONE##########################################
