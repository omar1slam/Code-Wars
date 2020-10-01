# Find anagrams of a word in a list
# https://www.codewars.com/kata/523a86aa4230ebb5420001e1/train/python
# 5 kyu



## abba
## baab
def anagrams(word, words):
    anags = []
    for w in words:
        temp = w
        check = list(word)
        if len(w) == len(word):
            while temp:
                if temp[0] in check:
                    for i in check:
                        if i == temp[0]:
                            check.remove(i)
                            break
                    temp = temp[1:]
                else:
                    break

            if not temp:
                anags.append(w)
    return anags

####################DONE##########################
## Much better solution========> def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]






