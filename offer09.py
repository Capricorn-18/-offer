"""请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )"""

# 创建一个队列，如果不给参数的话就返回一个null
# 创建两个列表用来装append函数和delete函数的值


class CQueue:

    def __init__(self):
        self.stackin = []
        self.stackout = []

    def appendTail(self, value: int) -> None:
        self.stackin.append(value)

    def deleteHead(self):
        # 如果stackout里面有元素的话， 则将其弹出
        if self.stackout:
           return self.stackout.pop()
        # 如果stackin里面没有元素，就说明没有进行append操作
        # 所以stackout肯定也是空的，所以返回-1
        elif not self.stackin:
            return -1
        else:
            # 如果stackin里面有元素的话，则使用stackout.append(self.stackin.pop())
            # 例如stackin是[5,2],通过上面操作，stackout就是【2,5】
            # 这样stackout.pop的时候输出的就是5， 2（类似于实现删除头部）
            while self.stackin:
                self.stackout.append(self.stackin.pop())
            return self.stackout.pop()