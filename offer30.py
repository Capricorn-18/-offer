class MinStack:

    def __init__(self):
        # 定义两个栈，分别用来存贮所有的元素，和非严格递减的元素
        # minstack用来存贮递减的元素，这样我们在使用min函数的时候，直接取出最后一个元素，时间复杂度就是O(1)
        self.stack = []
        self.minstack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minstack or x < self.minstack[-1]:
            self.minstack.append(x)

    def pop(self) -> None:
        # 对栈stack进行出栈操作，记为元素y, 如果y和minstack的栈顶元素（也就是最后一个元素）相等的话
        if self.stack.pop() == self.minstack[-1]:
            return self.minstack.pop()

    def top(self) -> int:
        # 返回栈顶元素，也就是列表的最后一个元素
        return self.stack[-1]

    def min(self) -> int:
        return self.minstack[-1]