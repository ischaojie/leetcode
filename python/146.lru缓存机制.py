#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

# @lc code=start
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    # 利用hash+双向链表实现
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}
        self.head = ListNode()
        self.tail = ListNode()
        # 初始化链表
        self.head.next = self.tail
        self.tail.prev = self.head


    # 查找key是否在hash表中
    def get(self, key: int) -> int:
        if key in self.hash:
            # key在hash表，则返回value，同时将这个key移到tail
            # 因为这个key刚刚被访问
            self.move_to_tail(key)
        res = self.hash.get(key, -1)
        if res == -1:
            return res
        else:
            return res.val
        
    # 如果key已经存在，更新value。如果key不存在，写入，当超出容积之后，删除最近最少使用。
    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            # key在hash表，更新value，同时将这个key移到tail
            self.hash[key].val = value
            self.move_to_tail(key)
        else:
            # 不在的话判断是否满了，然后插入
            # 如果满了
            if len(self.hash) == self.capacity:
                # 弹出链表开头的
                self.hash.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            # 新节点插入到tail
            new = ListNode(key, value)
            self.hash[key] = new
            new.prev = self.tail.prev
            new.next = self.tail
            self.tail.prev.next = new
            self.tail.prev = new
    
    # 将节点移到tail
    def move_to_tail(self, key):
        # 先将node断链
        node = self.hash[key]
        node.prev.next = node.next
        node.next.prev = node.prev

        # 然后将node移到tail
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node 

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

