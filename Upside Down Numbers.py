# Find all upside numbers withtin given range
#
# 3 kyu


import numpy as np
def is_ud(n):
    digits = [int(ch) for ch in str(n)]
    check = (len(digits) + 1) // 2
    return all(digits[i] + digits[-1 - i] == 10 for i in range(check))

def upn(st1,st2):
    n1 = int(st1)
    n2 = int(st2)
    counter = 0

    upsiders = ['1','0','8','9']

    for i in range(n1,n2):
        '''
        flag = 1
        temp = list(map(int, str(i)))
        st = str(i)
        temp = np.array(np.flip(temp))
        temp = int(''.join(map(str, temp)))
        if temp == i:
            for j in st:
                if j not in upsiders:
                    flag = 0
            if flag == 1:
                counter+=1
        '''
        if is_ud(i):
            counter+=1


    return counter





print(upn('0','25'))
