import heapq

# 官方堆实现优先级队列实现
class PriorityQueue:
    """
    优先级队列实现，利用 heapq 库，以最小堆实现
    """
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        """ 入队 """
        # 因为 heapq 实现的是最小堆，所有 prirority 为负数
        # 保证优先级高的先出队
        # index 可以保证优先级相同的时候，先入队的先出队
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        """ 出队 """
        return heapq.heappop(self._queue)[-1]


class PQueue:
    def __init__(self):
        # 队列元素
        self.elem = []
        # 队列元素个数
        self.n = 0

    def max(self):
        return self.elem[1]

    def push(self, k):
        """
        向堆末尾插入元素，上浮
        """
        self.n += 1
        self.elem[n] = k
        self._swim(self.n)

    def pop(self):
        """
        弹出堆顶元素
        """
        max = self.elem[1]
        self.elem[1], self.elem[self.n] = self.elem[self.n], self.elem[1]
        self.elem[n] = None
        self.n -= 1
        self._sink(1)
        return max

    def _parent(self, root):
        return root / 2

    def _left(self, root):
        return root * 2

    def _right(self, root):
        return root * 2 + 1

    def _swim(self, k):
        """
        上浮堆元素
        """
        # 父节点小于子节点，上浮
        while k > 1 and self.elem[self._parent(k)] < self.elem[k]:
            # 交换
            self.elem[self._parent(k)], self.elem[k] = (
                self.elem[k],
                self.elem[self._parent(k)],
            )
            # 继续比较下一个
            k = self._parent(k)

    def _sink(self, k):
        """
        下沉堆元素
        """
        while self._left(k) <= self.n:
            # 找出左右节点哪个更大
            older = self._left(k)
            if (
                self._right(k) <= self.n
                and self.elem[older] < self.elem[self._right(k)]
            ):
                older = self._right(k)
            # 如果 k 比子节点大，跳出
            if older < k:
                break
            # 交换
            self.elem[k], self.elem[older] = self.elem[older], self.elem[k]
            k = older


def test_pqueue():

    pqueue = PQueue()