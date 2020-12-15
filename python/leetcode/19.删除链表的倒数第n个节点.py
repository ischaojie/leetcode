#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        if not head or n <= 0:
            return head

        # 先循环获得链表长度
        count = 0 
        h = head
        # 边界控制
        p = ListNode(0)
        p.next = head
        while h:
            count += 1
            h = h.next

        count -= n
        
        h = p
        # 找到那个点
        while count > 0:
            count -= 1
            h = h.next
        
        h.next = h.next.next

        return p.next
            
# @lc code=end

