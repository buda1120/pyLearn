#CalHamletV1.py
def getText():
    txt = open("F:\Python_3.8.3\PRACTICE\CalText\hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./;:<>=?@[\\]^_`{|}~':
        txt = txt.replace(ch, " ")
    return txt

hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
#列表排序，对元素第二个字段排序，从大到小
items.sort(key = lambda x:x[1], reverse = True)
'''
key specifies a function of one argument that is used to extract
    a comparison key from each list element
    
key=lambda 元素: 元素[字段索引]
'''
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
