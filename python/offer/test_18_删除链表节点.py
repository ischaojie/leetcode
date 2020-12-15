# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        # 特殊情况
        if head == None:
            return None
        if head.val == val:
            return head.next
        

        # 定义一个指针
        curr = head
        # 走到要删除的节点处
        while curr.next != None and curr.next.val != val:
            curr = curr.next
        # 端链指向后面
        if curr.next != None:
            curr.next = curr.next.next
        
        return head
        
