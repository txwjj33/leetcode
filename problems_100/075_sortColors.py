'''
题目：颜色分类
描述：
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？
'''

'''
1趟遍历，0换到最左边，2换到最右边，48 ms
'''
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 0和2的当前位置index
        indexOf0, indexOf2 = 0, len(nums) - 1
        i = 0
        while i <= indexOf2:
            if nums[i] == 0:
                if i != indexOf0:
                    # 这种情况下nums[indexOf0]只能是1，如果是0的话，那么indexOf0应该更大
                    # 如果是2的话，会换到最后去了
                    nums[i], nums[indexOf0] = nums[indexOf0], nums[i]
                indexOf0 += 1
                i += 1
            elif nums[i] == 2:
                if nums[indexOf2] == 2:
                    indexOf2 -= 1
                else:
                    nums[i], nums[indexOf2] = nums[indexOf2], nums[i]
            else:
                i += 1
