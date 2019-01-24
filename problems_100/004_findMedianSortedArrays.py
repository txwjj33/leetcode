'''
题目：寻找两个有序数组的中位数
描述：
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
'''


'''
双指针逐步排除不可能区域，O(log(n1)) + O(log(n2 - n1))
设n = n1 + n2, mid = int((n - 1) / 2)
cur1,cur2分别指向nums1，nums2，且保持cur1+cur2=mid
比较nums1[cur1]和nums2[cur2]的大小，可以排除掉较小者左边的区间，以及较大者右边的区间
备注1：
可以通过如下的方法将nums1的长度变成n2或者n2 - 1，这样进行二分查找以后，nums2剩余的元素比较少，排序的时候比较快
这样处理以后时间复杂度大概O(log(n2))，处理之前的时间复杂度是O(log(n1)) + O(log(n2 - n1))
但是实际测试发现时间变长了，可能是这个转化比较费时
count = int((n2 - n1) / 2)
if count > 0:
    m = min(nums1[0], nums2[0]) - 1
    M = max(nums1[-1], nums2[-1]) + 1
    nums1 = [m] * count + nums1 + [M] * count
    n1 = len(nums1)
备注2：可以把每个元素重复两遍，这样list长度都变成偶数，而且中位数保持不变，但是那样可能比较耗时
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #为了方便处理，转化成n1 <= n2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # 先处理一些特殊情况
        n1, n2 = len(nums1), len(nums2)
        nums = None
        if n1 == 0:
            nums = nums2
        elif nums1[-1] <= nums2[0]:
            nums = nums1 + nums2
        elif nums1[0] >= nums2[-1]:
            nums = nums2 + nums1
        if nums:
            n = len(nums)
            # mid是中位数的下标，nums长度为偶数的话是第一个中位数的下标
            mid = int((n - 1) / 2)
            return nums[mid] if (len(nums) % 2 == 1) else ((nums[mid] + nums[mid + 1]) / 2)

        n = n1 + n2
        mid = int((n - 1) / 2)
        # [left, right]表示中位数可能在的闭区间，cur是二分查找指针，用于排除掉不可能存在的那些区间
        left1, right1, cur1 = 0, n1 - 1, int(n1 / 2)
        left2, right2, cur2 = 0, n2 - 1, mid - cur1
        while(right1 - left1 >= 2 and right2 - left2 >= 2):
            if nums1[cur1] <= nums2[cur2]:
                # 这种情况下，nums1中cur1左边的数都不可能是中位数
                # 因为nums1中从cur1往后的数都比它大，nums2中从cur2往后的数都比它大，比它大的数>=n-mid
                # 类似的，nums2中cur2以后的数也不可能是中位数
                left1 = cur1
                right2 = cur2
                # 因为n1 <= n2， 因此对n1做二分查找
                step = int((right1 - left1) / 2)
                cur1 += step
                cur2 -= step
            else:
                right1 = cur1
                left2 = cur2
                step = int((right1 - left1) / 2)
                cur1 -= step
                cur2 += step

        # 直接对剩余的数做排序，以下几种方法运行多
        # 方法1，调用系统函数排序，136 ms
        # remain = nums1[left1:right1 + 1] + nums2[left2:right2 + 1]
        # remain.sort()

        # 方法2, 双指针一次遍历两个数组，比较大小，108 ms
        i, j = left1, left2
        remain = []
        while(True):
            if i > right1:
                remain += nums2[j:right2 + 1]
                break
            if j > right2:
                remain += nums1[i:right1 + 1]
                break
            if nums1[i] <= nums2[j]:
                remain.append(nums1[i])
                i += 1
            else:
                remain.append(nums2[j])
                j += 1

        # 方法3， 把nums1的数字二分查找插入到nums2中，运行多次以后时间很不稳定，120ms-176ms
        # remain = nums2[left2:right2 + 1]
        # for i in range(left1, right1 + 1):
        #     t = nums1[i]
        #     left, right = 0, len(remain) - 1
        #     while(right - left > 1):
        #         cur = int((left + right) / 2)
        #         if t > remain[cur]:
        #             left = cur
        #         elif t < remain[cur]:
        #             right = cur
        #         else:
        #             left = cur
        #             break
        #     if t <= remain[left]:
        #         remain.insert(left, t)
        #     elif t <= remain[right]:
        #         remain.insert(right, t)
        #     else:
        #         remain.insert(right + 1, t)

        leftCount = left1 + left2
        if n % 2 == 0:
            return (remain[mid - leftCount] + remain[mid + 1 - leftCount]) / 2
        else:
            return remain[mid - leftCount]


'''
直接遍历排序，140 ms
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        if len(nums1) == 0:
            nums = nums2
        elif len(nums2) == 0:
            nums = nums1
        else:
            i, j = 0, 0
            while(True):
                if i >= len(nums1):
                    nums.extend(nums2[j:])
                    break
                if j >= len(nums2):
                    nums.extend(nums1[i:])
                    break
                if nums1[i] <= nums2[j]:
                    nums.append(nums1[i])
                    i += 1
                else:
                    nums.append(nums2[j])
                    j += 1

        n = len(nums)
        # mid是中位数的下标，nums长度为偶数的话是第一个中位数的下标
        mid = int((n - 1) / 2)
        return nums[mid] if (n % 2 == 1) else ((nums[mid] + nums[mid + 1]) / 2)
