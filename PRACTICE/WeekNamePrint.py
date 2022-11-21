#WeekNamePrint.py
weekStr = "星期一星期二星期三星期四星期五星期六星期天"
weekId = eval(input("请输入星期数值1-7："))
pos = (weekId - 1) * 3
print(weekStr[pos: pos + 3])
