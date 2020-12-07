
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def solution(preorder: list[int], inorder: list[int]) -> TreeNode:
    """
    前序和中序重建二叉树
    """

    # 中序遍历 [左子树，根节点，右子树]
    # 前序遍历 [根节点，左子树，右子树]
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    # 找到中序遍历中间位置
    mid = inorder.index(preorder[0])
    root.left = solution(preorder[1:mid+1], inorder[:mid])
    root.right = solution(preorder[mid+1:], inorder[mid+1:])
    return root
