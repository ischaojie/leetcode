class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def solution(head: ListNode)->list[int]:
    result = []
    
    while head:
        result.append(head.val)
        head = head.next
        
    return result[::-1]

def test_solution():
    # assert solution() == [5,4,3,2,1]
    pass
