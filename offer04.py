"""在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数
"""


# 思想：因为每一行的数字都是递增的，如果从矩阵的右上角看，则像是一颗二叉树
# 将输入值与右上角的值进行比较， 如果相等的话， 则直接返回该值
# 如果target比右上角的值大的话，则行加1否则就列减1
class Solution:
    def findNumberIn2DArray(self, matrix, target):
        n = len(matrix)
        if n == 0:
            return False
        row, col = 0, len(matrix[0]) - 1
        while row < n and col >= 0:
            if target == matrix[row][col]:
                return True
            if target < matrix[row][col]:
                col -= 1
            if target > matrix[row][col]:
                row += 1
        return False