#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 利用两个指针，依次相加并添加到res的末尾
        i, j = 0, 0

        res = ListNode(0)
        r = res
        temp = 0
        while l1 or l2:
            
            # 如果next为None，赋值为0
            i = l1.val if l1 else 0
            j = l2.val if l2 else 0
            s = temp + i + j
            # 获取进位数，满10进1
            temp = s // 10
            r.next = ListNode(s%10)
            
            r = r.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        # 末尾如果还有进位，则要加入1这个节点
        if temp > 0:
            r.next = ListNode(1)
        return res.next
# @lc code=end

