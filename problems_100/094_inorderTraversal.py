'''
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
44 ms, 6.5 MB
'''
class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        if not root: return []
        result = []
        temp = [root]
        visited = {}
        while len(temp) > 0:
            node = temp[-1]
            if (not node.left) or (node.left in visited):
                result.append(node.val)
                visited[node] = True
                temp.pop()
                if node.right:
                    temp.append(node.right)
            else:
                temp.append(node.left)
        return result


'''
40 ms, 6.5 MB
'''
class Solution:
    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        result = []
        stack = []
        while len(stack) > 0 or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                result.append(node.val)
                root = node.right
        return result