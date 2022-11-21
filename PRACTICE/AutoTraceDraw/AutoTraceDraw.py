#AutoTraceDraw.py
import turtle as t

#设置绘画环境
t.title("自动轨迹绘制")
t.setup(800, 600, 0, 0)
t.pencolor("red")
t.pensize(5)

#数据读取
datals = []
f = open("data.txt", 'r', encoding='utf-8', errors = "ignore")
f.readline()
next(f) #next():Python内置函数,返回迭代器的下一个项目
for line in f:
    line = line.replace("\n", "")
    datals.append(list(map(eval, line.split(","))))
f.close()

#自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3], datals[i][4], datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1] == 0:
        t.left(datals[i][2])
    else:
        t.right(datals[i][2])
