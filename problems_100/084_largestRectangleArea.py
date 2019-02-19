'''
题目：柱状图中最大的矩形
描述：
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。





以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。





图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。



示例:

输入: [2,1,5,6,2,3]
输出: 10
'''


'''
记录所有的数字出现的index，然后把数字排序，
遍历i，求i为左边界高度不定的矩形的最大面积
i右边的最小值是keys[0]，分两种情况考虑，
欲求矩形包含keys[0]，最大面积是keys[0] * (len(heights) - i)
欲求矩形不包含keys[0]，遍历j从i到keys[0]的位置，求最大面积
240 ms
'''
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        count = {}
        for i, h in enumerate(heights):
            count.setdefault(h, [])
            count[h].append(i)
        keys = list(count.keys())
        keys.sort()

        result = 0
        for i in range(len(heights)):
            # i右边的最小值是keys[0]，如果矩形包含keys[0]
            area = keys[0] * (len(heights) - i)
            if area > result: result = area

            m = heights[i]
            for j in range(i, count[keys[0]][0]):
                if heights[j] < m:
                    m = heights[j]
                area = m * (j - i + 1)
                if area > result: result = area

            h = heights[i]
            count[h].pop(0)
            if len(count[h]) == 0:
                keys.remove(h)
        return result



'''
分成两部分求解，分别求当期位置为边界的左右两个矩形的最大面积
其实也就是找左右两边比这个数更小的最近的位置
100 ms
'''
class Solution:
    # 记录一半的
    def halfLargestArea(self, heights, anotherAreas = None):
        length = len(heights)
        # 比当前位置数字更小的左边的第一个数字索引
        indexs = [-1] * length
        # 以当前位置的高度作为右边界的矩形的最大面积
        areas = [0] * length
        # areas的最大值
        result = 0
        for i in range(length):
            h = heights[i]
            if i == 0:
                indexs[i] = -1
            elif h > heights[i - 1]:
                indexs[i] = i - 1
            elif h == heights[i - 1]:
                indexs[i] = indexs[i - 1]
            else:
                index = indexs[i - 1]
                while index >= 0 and heights[index] >= h:
                    index = indexs[index]
                indexs[i] = index
            # [indexs[i] + 1， i]的面积
            areas[i] = h * (i - indexs[i])
            if anotherAreas:
                # i这个位置算了两遍，所以减掉h
                # areas和anotherAreas的顺序相反
                areas[i] += anotherAreas[length - 1 - i] - h
            if areas[i] > result:
                result = areas[i]
        return result, areas

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) == 0: return 0
        result, area = self.halfLargestArea(heights)
        heights.reverse()
        result, area = self.halfLargestArea(heights, area)
        return result


'''
递增栈: 从stack[i+1]往左边扫描，第一个比height[stack[i+1]]小的数字的下标就是stack[i]
所以可以推出height[stack[i]]<height[j], for j in (stack[i], stack[i+1]]
进一步能推出height[stack[i]]<height[j]，for j in (stack[i], stack[-1]]
同时因为height[stack[i]]<height[j]，for j in (stack[i-1], stack[i]]，
所以包含stack[i]的最大矩形就是(stack[i-1], stack[-1]]，在程序里stack[-1] = i - 1
高度是height[stack[i]]
60 ms, 9.1 MB
'''
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        l = len(heights)
        if l == 0:
            return 0
        if len(set(heights)) == 1:
            return l * heights[0]
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                t = stack[-1]
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        return ans
