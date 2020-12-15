#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
# 思路：
# 首先统计每个元素的个数，然后利用堆排序输出前k个元素
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 流氓解法
        from collections import Counter
        return [i[0] for i in Counter(nums).most_common(k)]
        


# @lc code=end

