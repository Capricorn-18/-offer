"""输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分"""

# 思想：用两个指针left,right分别指向左右两端，因为目标是想让偶数在右边，奇数在左边
# 1.如果左边为奇数，右边也为奇数，则left+1, right不变
# 2.如果左边为偶数，右边为偶数，则right-1 left不变
# 3.如果左边为奇数右边为偶数，则left+1，right-1
# 4.如果左边为偶数，右边为奇数，则左右元素互换位置
class Solution:
    def exchange(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            # 右边为奇数的时候
            if nums[right] % 2 != 0:
                if nums[left] % 2 != 0:
                    left += 1
                else:
                    nums[left], nums[right] = nums[right], nums[left]
            # 右边为偶数的时候
            else:
                if nums[left] % 2 != 0:
                    left += 1
                    right -= 1
                else:
                    right -= 1
        return nums


# 代码有点冗长，第13行的判断条件改成if nums[left] % 2 == 0后面的随之改变一下可以减少代码量

