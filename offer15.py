class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while True:
            if n % 2 == 1:
                count += 1
            n = n // 2
            if n == 0:
                break
        return count