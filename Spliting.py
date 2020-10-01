# split every two characters and add a _ in the end if it's odd
#
# 6 kyu

def split(sen):
    if len(sen) == 0:
        return []
    ans = ''
    if len(sen) % 2 != 0:
        sen += '_'
    for i in range(0,len(sen),2):
        if i != len(sen) - 2:
            ans += "".join(sen[i:i+2]) + ' '
        else:
            ans += "".join(sen[i:i + 2])
    return ans.split(' ')

##################DONE###################################