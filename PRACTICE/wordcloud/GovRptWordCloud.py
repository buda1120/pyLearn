#GovRptWordCloud.py
import jieba
import wordcloud
from imageio import imread

mask = imread("fivestart.png")

f = open("2021政府工作报告.txt", "r", encoding = "utf-8")
t = f.read()
f.close()

ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="msyh.ttc", width=1000, \
                        height=700, background_color="white", \
                        stopwords={"和", "的", "在", "等", "要", \
                                   "新", "对", "有", "好"},\
                        max_words=50, mask=mask)
w.generate(txt)
w.to_file("govrepwc.png")
