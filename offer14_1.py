# 方法1： 任何大于1的数都可以由2和3组成，又因为2*2*2<3*3
# 所以3的个数越多，则最后相乘的积越大


class Solution:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n
        result = 1
        # 为什么选n>4作为循环的条件：因为n=4的时候，最大乘积为4
        while n > 4:
            result *= 3
            n -= 3
        return result * n