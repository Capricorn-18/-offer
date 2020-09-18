"""一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法"""
# 通过徐找规律可以发现它和寻找斐波拉函数差不多，但是要注意n = 0时，跳法为1
class Solution:
    def numWays(self, n: int) -> int:
        if n < 3:
            return n
        # 创建一个长度为n值为0的列表，并为前三个元素赋值
        dp = [0] * n
        dp[0] = dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n] % 1000000007