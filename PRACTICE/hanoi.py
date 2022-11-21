#递归问题--汉诺塔hanoi

count = 0
def hanoi(n, src, dst, mid):
    global count

    #只剩一个盘，直接移动到目标杆
    if n == 1:
        print("{}:{}->{}".format(1, src, dst))
        count += 1
    else:
        #剩n个盘，把上面n-1个盘移到过渡杆
        hanoi(n-1, src, mid, dst)
        
        #最后一个盘移到目标杆，移动次数加1
        print("{}:{}->{}".format(n, src, dst))
        count += 1
        
        #将n-1个盘从过渡杆移到目标杆
        hanoi(n-1, mid, dst, src)
    

hanoi(4, "A", "B", "C")
print(count)
