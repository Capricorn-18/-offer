class Solution:
    def minArray(self, numbers):
        left, right = 0, len(numbers)-1
        while left < right:
            mid = left + right // 2
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                right = mid
            else:
                right -= 1


# 利用三个指针，left，mid, right
# 通过left+right//2得到mid的值
# 判断right和mid的值，如果mid的值>right的值的话，则left=mid+1
# 如果mid的值<right的值， right = mid
# 

