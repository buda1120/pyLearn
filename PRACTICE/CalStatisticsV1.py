#CalStatisticsV1.py

#获取用户不定长度输入
def getNum():
    nums = []
    iNumStr = input("请输入数字，回车退出:")
    while iNumStr != "":
        nums.append(eval(iNumStr))
        iNumStr = input("请输入数字，回车退出:")
    return nums


#求和
def getSum(numbers):
    sum = 0.0
    for num in numbers:
        sum += num
    return sum

#计算平均值
def getMean(numbers):
    s = 0.0
    for num in numbers:
        s += num
    return s / len(numbers)

#计算标准差（方差平方根）
def getDev(numbers, mean):
    s = 0.0
    for num in numbers:
        s += (num - mean) ** 2
    return pow((s / len(numbers)), 0.5)

#查看中位数
def getMedian(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size// 2 - 1] + numbers[size // 2]) / 2
        #数组的下标必须为整数，故使用 ‘//’操作符
    else:
        med = numbers[size // 2]
    return med

n = getNum()
m = getMean(n)
print("和：{}，平均值：{}，标准差：{:.2f}, 中位数：{}".format(getSum(n), m,
                                          getDev(n, m),getMedian(n) ))
