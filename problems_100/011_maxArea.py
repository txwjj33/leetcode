'''
题目：盛最多水的容器
描述：
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49
'''

'''
双指针法：O(n)，40 ms
说明：两个指针分别指向收尾，每次把高度较小的那个指针往中间移一格
证明：不妨设height[i] < height[j]，且[i, j]间的最大区域是f(i, j)，且最大区域对应的左指针设为t
当t = i时，因为height[i] < height[j]，最大的面积也不过是[i, j]之间的面积
当t > i时, 最大面积<= f(i + 1, j)
所以f(i, j) = max(height[i] * (j - i), f(i + 1, j))
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height) - 1
        r = 0
        while(i != j):
            if height[i] <= height[j]:
                area = (j - i) * height[i]
                i += 1
            else:
                area = (j - i) * height[j]
                j -= 1
            if area > r: r = area
        return r


'''
先记录每个高度的最大最小index，然后按逆序遍历高度，求最大的面积，O(n)
'''
class Solution(object):
    # 64 ms
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lines = {}
        for i in range(0, len(height)):
            h = height[i]
            if h in lines:
                lines[h][1] = i
            else:
                lines[h] = [i, i]

        r = 0
        start, stop = len(height), -1
        for h in sorted(lines.keys(), reverse = True):
            if h * len(height) <= r: break
            start = min(start, lines[h][0])
            stop = max(stop, lines[h][1])
            if (stop - start) * h > r:
                r = (stop - start) * h

        return r

    # 80ms, 这个更慢一些，不用排序，但是可能会有很多无用遍历
    def maxArea1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lines = {}
        hMax = 0
        for i in range(0, len(height)):
            h = height[i]
            if h > hMax: hMax = h
            if h in lines:
                lines[h][1] = i
            else:
                lines[h] = [i, i]

        r = 0
        start, stop = len(height), -1
        for h in range(hMax, 0, -1):
            if h * len(height) <= r: break
            if h not in lines: continue
            start = min(start, lines[h][0])
            stop = max(stop, lines[h][1])
            if (stop - start) * h > r:
                r = (stop - start) * h

        return r
