'''
题目：最接近的三数之和
描述：
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
'''


'''
先将数组排序，然后固定i，指针1指向i+1， 指针2指向末尾
把和鱼target比较，分别移动指针1或者指针2，类似于15题
88 ms
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = None
        for i in range(0, len(nums)):
            left, right = i + 1, len(nums) - 1
            while(left < right):
                s = nums[i] + nums[left] + nums[right]
                if s == target: return s
                if s < target:
                    left += 1
                else:
                    right -= 1
                if (closest == None) or abs(target - s) < abs(target - closest):
                    closest = s
        return closest

'''
这个方法是所有提交里最快的，其实主要思路跟我上面的方法差不多，就是做了几点优化：
1、nums[n1]==nums[n1-1]时，continue
2、最小的三个数>=target时，break
3、最大的三个数<=target时，continue
28 ms，速度快了很多，所有有些优化是有必要的
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n1=0
        ans=0
        dif=2**30
        lens=len(nums)
        while n1<lens-2:
            if nums[n1]==nums[n1-1] and n1>0:
                n1+=1
                continue
            n2=n1+1
            n3=lens-1
            tar=target-nums[n1]
            minx=nums[n2]+nums[n2+1]+nums[n1]
            if minx>target:
                if dif>minx-target:
                    dif=minx-target
                    ans=minx
                break
            maxx=nums[n1]+nums[n3]+nums[n3-1]
            if maxx<target:
                if dif>target-maxx:
                    dif=target-maxx
                    ans=maxx
                n1+=1
                continue
            while n2<n3:
                temp=nums[n2]+nums[n3]
                d=abs(tar-temp)
                if d==0:
                    return target
                if dif>d:
                    dif=d
                    ans=temp+nums[n1]
                if temp<tar:
                    n2+=1
                else:
                    n3-=1
            n1+=1
        return ans
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """