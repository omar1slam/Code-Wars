# No. of times you have to multiplicate the digits of a number till it's a one digit no.
# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python
# 6 kyu


def persistence(n,counter = 0):
    st = str(n)
    new_n = 1
    if len(st) == 1:
        return counter
    else:
       for x in st:
           new_n *= int(x)
       counter+=1
       return persistence(new_n,counter)


print(persistence(999))

#########################DONE##########################################