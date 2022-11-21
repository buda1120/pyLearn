#DayDayUp3.py
dayUp = 1.0
dayFactor = 0.01

for i in range(365):
    if i % 7 in [ 1, 2, 3, 4, 5]:
        dayUp = dayUp * (1 + dayFactor)
    else:
        dayUp = dayUp * (1 - dayFactor)
print("{:.2f}".format(dayUp))
