"""找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字
。"""


# 方法1：对列表进行排序，然后查看它附近的元素是否和它相同
# 时间复杂度：O(nlogn) 空间复杂度O(1)
class Solution:
    def findRepeatNumber(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                return nums[i]


# 方法2：哈希表
# 时间复杂度：O(n) 空间复杂度O(n)
class Solution2:
    def findRepeatNumber(self, nums):
        # 创建一个字典来装列表里面的元素
        repeatDict = {}
        for num in nums:
            # 如果元素不在字典里面，则将其放进字典，对应的value为1，如果在字典里面则直接返回该元素
            if num not in repeatDict:
                repeatDict[num] = 1
            else:
                return num


# 方法3：原地哈希，将元素放到它应该在的位置，位置i放元素i，如果位置上的元素和要归位的元素已经一样了，说明就重复了，重复了就return
class Solution3:
    def findRepeatNumber(self, nums):
        n = len(nums)
        for i in range(n):
            while i != nums[i]:
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                temp = nums[i]
                nums[temp], nums[i] = nums[i], nums[temp]