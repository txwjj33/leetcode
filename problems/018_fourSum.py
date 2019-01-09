'''
题目：四数之和
描述：
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

'''
跟一下方法基本一样，就是不事先判断等于的情况, 136 ms
使用sum函数、负数index、去掉事先判断等于的情况，代码简洁非常多
'''
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 4: return []
        nums.sort()
        r = []
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            ni = nums[i]

            diff = target - ni
            if sum(nums[i + 1:i + 4]) > diff: break
            if sum(nums[-3:]) < diff: continue

            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                nj = nums[j]
                diff = target - ni - nj

                if nums[j + 1] + nums[j + 2] > diff: break
                if nums[-2] + nums[-1] < diff: continue

                p1, p2 = j + 1, length - 1
                while p1 < p2:
                    np1, np2 = nums[p1], nums[p2]
                    if np1 + np2 == diff:
                        r.append([ni, nj, np1, np2])
                    if np1 + np2 <= diff:
                        while (p1 < p2 and nums[p1] == np1):
                            p1 += 1
                    else:
                        while (p1 < p2 and nums[p2] == np2):
                            p2 -= 1

        return r

'''
排序以后，固定前两个数，后两个数用双指针法，128 ms
双指针法优先排除最小两个数之和、最大两个数之和
'''
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 4: return []
        nums.sort()
        r = []
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            ni = nums[i]

            # 如果不事先判断这个smallest和bigest，则时间是188ms
            smallest = ni + nums[i + 1] + nums[i + 2] + nums[i + 3]
            if smallest == target:
                r.append([ni, nums[i + 1], nums[i + 2], nums[i + 3]])
            if smallest >= target:
                break

            bigest = ni + nums[length - 3] + nums[length - 2] + nums[length - 1]
            if bigest == target:
                r.append([ni, nums[length - 3], nums[length - 2], nums[length - 1]])
            if bigest <= target:
                continue

            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                nj = nums[j]
                diff = target - ni - nj

                # 如果也不事先判断这个smallest和bigest，则时间是1856 ms
                smallest = nums[j + 1] + nums[j + 2]
                if smallest == diff:
                    r.append([ni, nj, nums[j + 1], nums[j + 2]])
                if smallest >= diff:
                    break

                bigest = nums[length - 2] + nums[length - 1]
                if bigest == diff:
                    r.append([ni, nj, nums[length - 2], nums[length - 1]])
                if bigest <= diff:
                    continue

                p1, p2 = j + 1, length - 1
                while p1 < p2:
                    np1, np2 = nums[p1], nums[p2]
                    if np1 + np2 == diff:
                        r.append([ni, nj, np1, np2])
                    if np1 + np2 <= diff:
                        while (p1 < p2 and nums[p1] == np1):
                            p1 += 1
                    else:
                        while (p1 < p2 and nums[p2] == np2):
                            p2 -= 1

        return r
