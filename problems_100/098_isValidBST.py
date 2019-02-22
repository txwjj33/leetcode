'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
中序遍历升序
60 ms, 9.2 MB
'''
class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        pre = None
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                if pre != None and node.val <= pre:
                    return False
                pre = node.val
                root = node.right
        return True


'''
递归，同时返回最小最大值
64 ms, 9.7 MB
'''
class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        if not root: return True
        result, _, _ = self.helper(root)
        return result

    def helper(self, root):
        v = root.val
        if not root.left and not root.right:
            return True, v, v

        mRes, MRes = v, v
        if root.left:
            result, m, M = self.helper(root.left)
            if not result: return False, m, M
            if M >= v:
                return False, m, M
            mRes = m

        if root.right:
            result, m, M = self.helper(root.right)
            if not result: return False, m, M
            if m <= v:
                return False, m, M
            MRes = M

        return True, mRes, MRes
