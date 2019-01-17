'''
题目：搜索旋转排序数组
描述：
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
'''

'''
先把target和nums[-1]比较，确定目标在左边还是右边
56 ms
'''
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0: return -1
        if target == nums[-1]:
            return len(nums) - 1
        inLeft = (target > nums[-1])
        left, right = 0, len(nums)
        while left < right:
            mid = int((left + right) / 2)
            n = nums[mid]
            if target == n: return mid

            if inLeft:
                if n > nums[0]:
                    if target > n:
                        left = mid + 1
                    else:
                        right = mid
                else:
                    # n在右边那一段，不可能找到target
                    right = mid
            else:
                if n > nums[-1]:
                    # n在左边那一段，不可能找到target
                    left = mid + 1
                else:
                    if target > n:
                        left = mid + 1
                    else:
                        right = mid

        return -1
