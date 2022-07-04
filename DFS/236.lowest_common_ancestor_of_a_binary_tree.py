# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 合并
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        return None

# 分开 清晰 但会超时
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        # 如果p,q为根节点，则公共祖先为根节点
        if root == p or root == q:
            return root
        # 如果p,q在左子树，则公共祖先在左子树查找
        if self.find(root.left, p) and self.find(root.left, q):
            return self.lowestCommonAncestor(root.left, p, q)
        # 如果p,q在右子树，则公共祖先在右子树查找
        if self.find(root.right, p) and self.find(root.right, q):
            return self.lowestCommonAncestor(root.right, p, q)
        # 如果p, q分属两侧，则公共祖先为根节点
        return root

    # find 相当于重复做了一次遍历操作
    def find(self, root, c):
        if not root:
            return False
        if root == c:
            return True
        return self.find(root.left, c) or self.find(root.right, c)
