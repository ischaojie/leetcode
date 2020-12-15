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
        # 队列元素索引
        self.index = 0

    def max(self):
        return self.elem[1]

    def push(self, elem):
        """
        向堆末尾插入元素，上浮
        """
        self.index += 1
        self.elem[self.index] = elem
        self._swim(self.index)

    def pop(self):
        """
        弹出堆顶元素
        """
        max = self.elem[1]  # 最大的是堆顶
        # 将堆末尾元素放到堆顶
        self.elem[1], self.elem[self.index] = self.elem[self.index], self.elem[1]
        # 将堆末尾元素弹出（替换下来的）
        self.elem.pop()
        self.index -= 1
        # 下沉
        self._sink(1)
        return max

    def _swim(self, k):
        """
        上浮堆元素
        """
        # 父节点小于子节点，上浮
        parent = k >> 1
        while k > 1 and self.elem[parent] < self.elem[k]:
            # 交换
            self.elem[parent], self.elem[k] = self.elem[k], self.elem[parent]
            # 继续比较下一个
            # 从父节点开始，比较父节点和父父节点大小
            k = parent

    def _sink(self, k):
        """
        下沉堆元素
        """
        left, right = k << 1, k << 1 + 1
        # 循环，当 k 左节点 小于 index
        while left <= self.index:
            # 找出左右节点哪个更大，大的和父节点 k 交换
            # 先假设大的为 left
            older = left
            # 如果 left 小于 right，将大的设为 right
            if right <= self.index and self.elem[older] < self.elem[right]:
                older = right
            # 如果 k 比子节点大，跳出
            if older < k:
                break
            # 交换
            self.elem[k], self.elem[older] = self.elem[older], self.elem[k]
            # 往下继续
            k = older


def test_pqueue():

    pqueue = PQueue()
    pqueue.push(3)
    pqueue.push(5)
    pqueue.push(2)
    assert pqueue.pop() == 5
