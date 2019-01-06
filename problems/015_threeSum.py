'''
题目：三数之和
描述：
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

'''
把正负数的个数分别存在d1，d2里，依次考虑以下可能的情况，
3个0， 1个0 1正1负，2负1正，2正1负
480 ms
'''
class Solution(object):
    def find(self, d1, d2, r):
        d1Keys = list(d1.keys())
        for i in range(0, len(d1Keys)):
            n = d1Keys[i]
            if d1[n] >= 2:
                if - 2 * n in d2: r.append([n, n, -2 * n])
            for j in range(i + 1, len(d1Keys)):
                m = d1Keys[j]
                if - n - m in d2: r.append([n, m, - n - m])

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d1, d2 = {}, {}
        zero = 0
        for n in nums:
            if n > 0:
                d2.setdefault(n, 0)
                d2[n] += 1
            elif n < 0:
                d1.setdefault(n, 0)
                d1[n] += 1
            else:
                zero += 1
        r = []
        if zero >= 3:
            r.append([0, 0, 0])
        if zero >= 1:
            for n in d1:
                if -n in d2: r.append([n, 0, -n])
        self.find(d1, d2, r)
        self.find(d2, d1, r)
        return r


'''
先将数组排序，然后固定i，指针1指向i+1， 指针2指向末尾
如果和大于0，则指针2往左移一个
如果和小于0，则指针1往右移一个
如果和等于0，就是寻找到的目标
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res =[]
        i = 0
        for i in range(len(nums)):
            if i == 0 or nums[i]>nums[i-1]:
                l = i+1
                r = len(nums)-1
                while l < r:
                    s = nums[i] + nums[l] +nums[r]
                    if s ==0:
                        res.append([nums[i],nums[l],nums[r]])
                        l +=1
                        r -=1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while r > l and nums[r] == nums[r+1]:
                            r -= 1
                    elif s>0:
                        r -=1
                    else :
                        l +=1
        return res


'''
对正负数集合做两层循环找相反数，428 ms
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
            else:
                dic[n] = 1
        if 0 in dic and dic[0] >= 3:
            r = [[0, 0, 0]]
        else:
            r = []

        pos = [n for n in dic if n > 0]
        neg = [n for n in dic if n < 0]
        for p in pos:
            for n in neg:
                t = - (p + n)
                if t in dic:
                    if t == p and dic[p] > 1:
                        r.append([n, p, p])
                    elif t == n and dic[n] > 1:
                        r.append([n, n, p])
                    elif t < n or t > p or t == 0:
                        r.append([n, t, p])
        return r