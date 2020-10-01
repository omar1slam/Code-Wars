# Transofrm array to a snailshell pattern
# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/python
# 4 kyu

def snail(array):
    n = len(array)
    ans = []
    i = 0
    j = -1
    direction = 'right'
    k = 1
    if len(array) == 1:
        return array[0]

    while len(ans) < n*n:
        if direction == 'right':
            j += 1
            if j == n - k:
                direction = 'down'
            ans.append(array[i][j])

        elif direction == 'down':
            i += 1
            if i == n - k:
                direction = 'left'
            ans.append(array[i][j])

        elif direction == 'left':
            j -= 1
            if j == k-1:
                direction = 'up'
            ans.append(array[i][j])

        elif direction == 'up':
            i -= 1
            if i == k:
                direction = 'right'
                k += 1
            ans.append(array[i][j])

    return ans






array = [[1,2,3,4,5,6],
         [20,21,22,23,24,7],
         [19,32,33,34,25,8],
         [18,31,36,35,26,9],
         [17,30,29,28,27,10],
         [16,15,14,13,12,11]]
b =[]
## 00,01,02,12,22,21,20,10,11
## 00->0n-1,0n-1->n-1n-1,n-1n-1=>0n-1,
#print(array[0].reverse())

##################################DONE###########################
