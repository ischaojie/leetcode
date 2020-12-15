#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # 利用层次遍历
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        res = ""
        while queue:
            node = queue.pop(0)
            if node:
                res += str(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res += "null"
            res += " "
        return res
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split()
        print(data)
        if data[0] == "null": return None
        root = TreeNode(int(data[0]))
        queue = [root]
        i = 1
        while queue:
            node = queue.pop(0)
            if node == None:
                continue
            node.left = TreeNode(int(data[i])) if data[i] != 'null' else None
            node.right = TreeNode(int(data[i+1])) if data[i+1] != 'null' else None
            i += 2
            queue.append(node.left)
            queue.append(node.right)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

