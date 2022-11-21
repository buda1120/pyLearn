#chnwcloud
import jieba
import wordcloud

txt = "\
计算机程序（Computer Program），\
港、台译做电脑程式。计算机程序是\
一组计算机能识别和执行的指令，\
运行于电子计算机上，满足人们某种\
需求的信息化工具。它以某些程序设计\
语言编写，运行于某种目标结构体系上。"
cnstopwords = {"的", "于", "它", "是", "和"}

w = wordcloud.WordCloud(width = 1000, \
      font_path = "msyh.ttc", height = 700, \
    stopwords=cnstopwords)
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("chnwcloud.png")
