class Solution:
    def minCount(self, coins: List[int]) -> int:
        res = 0
        for i in range(len(coins)):
            if coins[i] % 2 == 0:
                count = coins[i] // 2
                res += count
            else:
                count = coins[i] // 2 + 1
                res += count
        return res