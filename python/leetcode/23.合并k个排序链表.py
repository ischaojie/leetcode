#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 递归两两合并
        if lists is None:
            return
        return self.merge(lists, 0, len(lists)-1)
    
    def merge(self,lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.merge2Lists(l1, l2)

    def merge2Lists(self, l1, l2):
        if l1 is None: return l2
        if l2 is None: return l1
        if l1.val < l2.val:
            l1.next = self.merge2Lists(l1.next, l2)
            return l1
        else:
            l2.next = self.merge2Lists(l1, l2.next)
            return l2
# @lc code=end

