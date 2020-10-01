## Find the consecutive product of fib no's
## https://www.codewars.com/kata/5541f58a944b85ce6d00006a/train/python
## 5 kyu

def productFib(prod):
    fibs = [0,1]
    i = 2
    while 1:
        fibs.append(fibs[i-1] + fibs[i-2])
        if (fibs[i-1] * fibs[i-2]) == prod:
            return [fibs[i-2], fibs[i-1], True]
        elif (fibs[i-1] * fibs[i-2]) > prod:
            if (fibs[i-3] * fibs[i-2]) < prod:
                return [fibs[i-2], fibs[i-1], False]
        i+=1


print(productFib(13*8))

####################################DONE##################################