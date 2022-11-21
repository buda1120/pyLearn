#DayDayUp4.py

def dayUp(df):
    dayUp = 1
    for i in range(365):
        if i%7 in [0, 6]:
            dayUp = dayUp * (1 - 0.01)
        else:
            dayUp = dayUp * (1 + df)
    return dayUp
    
dayFactor = 0.01
total = pow(1.01, 365)
while dayUp(dayFactor) < total:
    dayFactor += 0.001
print("工作日的努力参数：{:.3f}".format(dayFactor))
