#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 说明：解集不能包含重复的子集。
#
from typing import List

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.backtrack(0, [], nums)
        return self.result

    def backtrack(self, start, track, nums):
        # 将当前 track 加入
        # 为啥不像全排列，判断终止条件
        # 因为每个子集都可加入，而不是要全部元素都在才行
        self.result.append(track[:])
        
        # 设置 start 的位置不同（向后迭代），保证子集不重复
        # 因为[1,2] 和 [2,1]是一样的
        for i in range(start, len(nums)):
            track.append(nums[i])
            self.backtrack(i+1, track, nums)
            track.pop()            
        
# @lc code=end

def test_solution():
    result = Solution().subsets([1,2,3])
    print(result)

