""" 
有三根杆（编号A、B、C），在A杆自下而上、由大到小按顺序放置n个盘子（编号从n至1，即最下面盘子编号为n，最上面盘子编号为1）。
目标：把A杆上的盘子全部移到C杆上，并仍保持原有顺序叠好。
操作规则：每次只能移动一个盘子，并且在移动过程中三根杆上都始终保持大盘在下，小盘在上，操作过程中盘子可以置于A、B、C任一杆上。
提示：编写递归函数解决该问题。

输入格式:盘子个数n。

输出格式：每一行输出一个盘子移动的操作，格式为：盘子编号:原杆编号->目标杆编号。 """

def mov(i, start, dest):
    print('%d:%s->%s'%(i, start, dest))

def hanoi(n, start, mid, dest):
    if n == 1:
        mov(n, start, dest)
    else:
        hanoi(n-1, start, dest, mid) #将上n-1个盘移到mid柱
        mov(n, start, dest) #将最下面一个盘移到dest柱
        hanoi(n-1, mid, start, dest) #将n-1个盘移到dest柱

if __name__ == '__main__':
    n = eval(input())
    hanoi(n, 'A', 'B', 'C')
