'''
题目：下一个排列
描述：
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

'''
逆序遍历，如果单调增加，则continue，遇到变小的数，找到大于它的最小数字，跟它对调
右边的其他数字两两对调，就是升序排列。
76 ms
'''
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0: return
        M = nums[-1]
        for i in range(-2, - len(nums) - 1, -1):
            n = nums[i]
            if n >= M:
                M = n
                continue
            # 找到比n大的最小的数，注意这里都是负数坐标
            j = i + 1
            while j < 0 and n < nums[j]:
                j += 1
            # j - 1的数是要放在i位置的数
            nums[i], nums[j - 1] = nums[j - 1], nums[i]
            p1, p2 = i + 1, -1
            while p1 < p2:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                p2 -= 1
            return

        # 原数组降序排列，改成升序
        nums.reverse()
