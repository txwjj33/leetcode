'''
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
64 ms, 7.5 MB
'''
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0: return []
        from collections import defaultdict
        cache = defaultdict(list)

        def helper(start, end):
            if start > end: return [None]
            if (start, end) in cache:
                return cache[(start, end)]
            for i in range(start, end + 1):
                for left in helper(start, i - 1):
                    for right in helper(i + 1, end):
                        root = TreeNode(i)
                        root.left, root.right = left, right
                        cache[(start, end)].append(root)
            return cache[(start, end)]

        return helper(1, n)
