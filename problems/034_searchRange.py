'''
题目：在排序数组中查找元素的第一个和最后一个位置
描述：
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
'''

'''
先找到一个等于target的数，然后在左右两边分别寻找第一个位置和最后一个位置
48 ms
'''
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0: return [-1, -1]
        left, right, index = 0, len(nums), -1
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1

        if index == -1: return [-1, -1]
        result = [index, index]
        low, high = left, index
        # 从[left, index]中找第一个位置
        while low < high:
            mid = int((low + high) / 2)
            if nums[mid] == target:
                result[0] = mid
                high = mid
            else:
                low = mid + 1

        # 从[index, right]中找到最后一个位置
        low, high = index + 1, right
        while low < high:
            mid = int((low + high) / 2)
            if nums[mid] == target:
                result[1] = mid
                low = mid + 1
            else:
                high = mid
        return result
