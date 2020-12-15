#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
思路：利用尾插法，pre，和tail两个指针指向k个长度的链表两端。
首先，tail移动到k个大小的末尾，
然后将pre的下一个元素cur断链，
cur = pre.next
pre.next = cur
插入到tail的后面，
cur.next = tail.next
tail.next = cur
处理完成这一段之后，循环tail继续走k个大小的位置。
"""

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 尾插法
        dummy = ListNode(0)
        dummy.next = head

        pre, tail = dummy, dummy

        while True:
            count = k
            # tail走到第k个位置
            while count and tail:
                count -= 1
                tail = tail.next
            # 如果走到最末尾了，退出循环
            if not tail: break

            head = pre.next
            # 依次把cur移到tail的后面
            while pre.next != tail:
                # 当前节点
                cur = pre.next
                # 将cur断链
                pre.next = cur.next
                # 将cur移到tail的后面
                # cur断开指向tail的下一个，然后tail接cur
                cur.next = tail.next
                tail.next = cur
            pre = head
            tail = head
        return dummy.next
# @lc code=end

