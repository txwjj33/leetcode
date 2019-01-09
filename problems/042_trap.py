'''
题目：接雨水
描述：
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:

输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
'''

'''
从左往右求一次，如果最大值不在右边，再把从右边到最大值中间的求一遍，52 ms
'''
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2: return 0
        r = 0       # 最终的值
        temp = 0    # 从cur到当前累积的值，只有遇到一个大于等于cur的数才会作为确定值，加到r中
        cur, curIndex = height[0], 0
        for i in range(len(height)):
            h = height[i]
            if h >= cur:
                cur, curIndex = h, i
                r += temp
                temp = 0
            else:
                temp += cur - h

        if curIndex == len(height) - 1:
            return r

        # 最大值在中间，从末尾到cur再求一次
        cur = height[-1]
        for i in range(-1, curIndex - len(height), -1):
            h = height[i]
            if h >= cur:
                cur = h
            else:
                r += cur - h

        return r


'''
先找到最大值，然后从这个位置左右分成两段，分别从首尾开始求值，68 ms
'''
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 2: return 0
        maxHeight, index = height[0], 0
        for i in range(len(height)):
            if height[i] >= maxHeight:
                maxHeight = height[i]
                index = i
        if maxHeight == 0: return 0

        r = 0
        for i in range(index + 1):
            if height[i] > height[0]:
                height[0] = height[i]
            else:
                r += height[0] - height[i]

        # 注意反向遍历的时候首尾最好都是用负数，这样如果遍历全表不会出错
        # 否则用正数的话应该是(len(height) - 1, index - 1, -1)
        # 当index = 0时，上述表达式的结果是空
        for i in range(-1, index - 1 - len(height), -1):
            if height[i] > height[-1]:
                height[-1] = height[i]
            else:
                r += height[-1] - height[i]

        return r

