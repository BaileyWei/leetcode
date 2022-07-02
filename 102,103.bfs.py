# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 102
class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            # 翻转 变左->右
            queue = queue[::-1]
            temp_queue, l = [], []
            count = len(queue)
            while count > 0:
                # 从右边pop 添加
                node = queue.pop()
                l.append(node.val)
                # 从右边加
                if node.right:
                    temp_queue.append(node.right)
                if node.left:
                    temp_queue.append(node.left)
                count -= 1
            queue = temp_queue
            # 翻转
            res.append(l[::-1])
        return res

# 103 zigzag
# 多一个flag判断要不要翻转添加
class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        queue = [root]
        flag = True
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            flag = not flag
            queue = queue[::-1]
            temp_queue, l = [], []
            count = len(queue)
            while count > 0:
                node = queue.pop()
                l.append(node.val)

                if node.right:
                    temp_queue.append(node.right)
                if node.left:
                    temp_queue.append(node.left)
                count -= 1
            queue = temp_queue
            if flag:
                res.append(l)
            else:
                res.append(l[::-1])
        return res