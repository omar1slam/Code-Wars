# Is the number 1 the lonlinest digit
# https://www.codewars.com/kata/5dfa33aacec189000f25e9a9/train/python
# 6 kyu

def loneliest(number):
    minLon = 50
    lng = str(number)
    store = []
    for i in range(len(lng)):
        x = i - int(lng[i])
        y = i + int(lng[i]) + 1
        if x < 0:
            x = 0
        if y > (len(lng)):
            y = len(lng)
        temp = lng[x:y]
        lon = sum(int(digit) for digit in temp) - int(lng[i])
        if lon <= minLon:
            minLon = lon
            if int(lng[i]) == 1:
                store.append(lon)

    if len(store)!=0:
        store = sorted(store)
        if store[0] == minLon:
            return True
        else:
            return False
    else:
        return False

n = 123456

print(loneliest(n))


#########################DONE##########################################