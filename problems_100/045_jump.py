'''
题目：跳跃游戏 II
描述：
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。
'''

'''
动态规划，从后往前求所有的，96 ms
'''
class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1: return 0
        # steps[i]表示从i位置跳到末尾需要的最小步数
        steps = {len(nums) - 1: 0}
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= len(nums) - 1:
                steps[i] = 1
                continue

            steps[i] = len(nums)
            for j in range(nums[i], 0, -1):
                steps[i] = min(steps[i], 1 + steps[i + j])
                if steps[i] == 2:
                    # steps[i]最小只能是2，不能更小了，所以可以break
                    break

        return steps[0]


'''
52 ms
'''
class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=len(nums)-1
        j=0;maxs=0;result=0

        while j<k:
            if nums[j]==1:
                j+=1;result+=1

            elif nums[j]+j>=k:
                return result+1
            else:
                maxs=1+nums[j+1]
                sym=1
                for i in range(1,nums[j]+1):
                    if i+nums[j+i]>maxs:
                        maxs=i+nums[j+i]
                        sym=i

                j+=sym;result+=1

        return result

'''
56 ms
'''
class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        farthest = 0
        end = 0
        res = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                res += 1
                end = farthest
        return res