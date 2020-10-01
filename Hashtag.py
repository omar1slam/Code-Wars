## Generate Hashtags
## https://www.codewars.com/kata/52449b062fb80683ec000024/train/python
## 5 kyu

def generate_hashtag(s):
    if s == '':
        return False
    hsh = '#'
    x = s.split(' ')
    for i in range(len(x)):
        x[i] = x[i].capitalize()

    s = ' '.join(x)
    a = s.replace(' ', '')
    if len(a) > 140:
        return False
    else:
        return hsh + a

print(generate_hashtag())

##########################################DONE##################################