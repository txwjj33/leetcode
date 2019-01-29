'''
题目：搜索旋转排序数组 II
描述：
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。

编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。

示例 1:

输入: nums = [2,5,6,0,0,1,2], target = 0
输出: true
示例 2:

输入: nums = [2,5,6,0,0,1,2], target = 3
输出: false
进阶:

这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
'''

'''
48 ms
先找到first，使得nums[first]和nums[-1]不一样，方便后面处理
'''
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if len(nums) == 0: return False
        if target == nums[-1]: return True
        # 先找到first，使得nums[first]和nums[-1]不一样，方便后面处理
        first = -1
        for i in range(0, len(nums)):
            if nums[i] != nums[-1]:
                first = i
                break
        # 所有数都一样
        if first == -1: return False
        if target == nums[first]: return True

        left, right = first, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                if nums[mid] < nums[first] < target:
                    right = mid
                else:
                    left = mid + 1
            else:
                if target < nums[first] <= nums[mid]:
                    left = mid + 1
                else:
                    right = mid
        return False
