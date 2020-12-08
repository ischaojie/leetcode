from typing import List


"""
使用辅助栈
"""


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        # * 先将所有pushed的元素入辅助栈
        for em in pushed:
            stack.append(em)
            # 同时每次判断当前栈顶元素是否等于 popped 对应元素
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        # * 如果最终下来栈空了，说明压入和弹出操作合法    
        return not stack
