#CalThreeKingdomsV2.py
#去除不属于人名的词组
import jieba
txt = open("threekingdoms.txt", "r", encoding = "utf-8").read()
excludes = {"却说", "二人", "不可", "荆州", "不能", "如此", "如何", "商议",
            "左右", "军马", "军士", "引兵", "次日", "大喜", "天下"}
words = jieba.lcut(txt)
counts = {}

for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1

for word in excludes:
    del counts[word]

items = list(counts.items())
items.sort(key = lambda x:x[1], reverse = True)
for i in range(10):
    name, count = items[i]
    print("{0:<10}{1:>5}".format(name, count))
