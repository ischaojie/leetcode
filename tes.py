class Solution:
    
    def __init__(self, root, k):
        res = self.search(root)
        return res[k-1]
        
    def search(self, root):
        if root is None:
            return []
        res = []
        
        if res.left:
            res += self.search(root.left)
        res.append(root.val)
        if res.right:
            res += self.search(root.right)
        return res

if __name__ == '__main__':
    tree = [1,2,3,4,5,6,7]
    res = Solution(tree, 2)
    print(res)