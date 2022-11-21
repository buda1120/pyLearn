#SevenDigitDrawV1.py
import turtle as t
import time

#画线
def drawLine(draw):
    t.pendown() if draw else t.penup()
    t.fd(60)
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
    for i in date:
        drawDigit(eval(i))

    
#主函数
def main():        
    t.setup(800, 350, 200, 200)
    t.penup()
    t.fd(-350)
    date = time.strftime("%Y%m%d", time.gmtime())
    print(date)
    drawDate(date)
    t.hideturtle()
    t.done()
main()
