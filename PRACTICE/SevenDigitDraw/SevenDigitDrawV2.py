#SevenDigitDrawV2.py
import turtle as t
import time

#绘制数码管间隔
def drawGap():
    t.penup()
    t.fd(5)

#画线
def drawLine(draw):
    drawGap()
    t.pendown() if draw else t.penup()
    t.fd(40)
    drawGap()
    t.right(90)


#画数码管
def drawDigit(digit):
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
    t.left(90)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)

    t.left(180)
    t.penup()
    t.fd(30)
    
  
#画日期
def drawDate(date):
    t.pencolor("red")
    count = 0
    for i in date:
        if i in ['-', ":", " "]:
            if count == 0:
                t.write("年", font=("Arial", 18, "normal"))
                t.pencolor("green")
            elif count == 1:
                t.write("月", font=("Arial", 18, "normal"))
                t.pencolor("blue")
            elif count == 2:
                t.write("日", font=("Arial", 18, "normal"))
                t.pencolor("purple")
            elif count == 3:
                t.write("时", font=("Arial", 18, "normal"))
                t.pencolor("blue")
            elif count == 4:
                t.write("分", font=("Arial", 18, "normal"))
                t.pencolor("green")
            t.fd(35)
            count += 1
        else:
            drawDigit(eval(i))

    
#主函数
def main():        
    t.setup(1400, 350, 100, 300)
    t.penup()
    t.fd(-650)
    date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #print(date)
    drawDate(date)
    t.write("秒", font=("Arial", 18, "normal"))
    t.hideturtle()
    t.done()
main()
