class CQueue:
    """
    每次将第一个队列全部移到第二个队列
    然后每次取第二个队列top
    """

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def appendTail(self, value: int) -> None:
        self.in_stack.append(value)

    def deleteHead(self) -> int:

        if self.out_stack:
            return self.out_stack.pop()
        elif not self.in_stack:
            return -1
        else:
            while len(self.in_stack) > 0:
                self.out_stack.append(self.in_stack.pop())
            return self.out_stack.pop()
# Test


obj = CQueue()
obj.appendTail(3)
print(obj.deleteHead())
print(obj.deleteHead())
print(obj.deleteHead())


# obj.deleteHead()
