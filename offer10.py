class Solution:
    def fib(self, n: int) -> int:
        # 如果 n=0,1的话，则返回0.1
        if n < 2:
            return n
        a, b = 1, 0
        # 实现 0+1+2+3+.......
        # n个数相加，只需要进行n-1次加法所以次数i从1到n
        for i in range(1, n):
            a = a + b
            b = a
            i += 1
        return a % 1000000007