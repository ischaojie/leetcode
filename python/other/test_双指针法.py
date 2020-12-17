class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 判断链表是否有环
def has_cycle(head: ListNode):
    fast, slow = head
    while fast != None and fast.next != None:
        # fast 走两步
        fast = fast.next.next
        # slow 走一步
        slow = slow.next

        if fast == slow:
            return True
    return False


# 反转数组
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


def test_reverse_array():
    assert reverse_array([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
