class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def sumofDigit(x, y):
            result = 0
            # 把x才分为十位数和百位数，然后进行相加
            while x > 0:
                result += x % 10
                x //= 10

            # 把x才分为十位数和百位数，然后进行相加
            while y > 0:
                result += y % 10
                y //= 10
            return result

        def dfs(i, j):
            if i == m or j == n or sumofDigit(i, j) > k or (i, j) in marked:
                return

            marked.add((i, j))
            dfs(i + 1, j)
            dfs(i, j + 1)
        # 用来贮存可以到达的坐标，然后根据长度来进行计算
        marked = set()
        dfs(0, 0)
        return len(marked)
