#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        # 利用三个flag，k控制外循环，i和j控制内循环
        # 关键：跳过重复的
        res = []
        for k in range(len(nums)-2):
            # 
            if nums[k] > 0:
                break
            # 当前的和前一个k相同，跳过重复的
            if k > 0 and nums[k] == nums[k-1]:
                continue
            
            # i, j一前一后
            i, j = k + 1, len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                # 如果三数之和大于0
                if s < 0:
                    i += 1
                    # 有重复的就跳过
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    # 跳过重复的
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                else:
                    # 加入
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    # 有重复跳过
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
        return res


        
# @lc code=end

