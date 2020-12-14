class Solution:

    def permute(self, nums: list[int]) -> list[list[int]]:
        self.result = []
        self.backtrack([], nums)
        return self.result
    # 回溯
    # track 代表每条路径，nums 代表选择列表
    # 每次从选择列表中拿出一个放入 track 中
    def backtrack(self, track, nums):
        # 终止条件：该条路径找完了
        if len(track) == len(nums):
            # 这里为啥要用 trackp[:]，因为这样就相当于复制了一份
            # 否则在后面循环的时候，track.pop()，track 都是空的
            # 因为 list 是个引用类型
            self.result.append(track[:])
            return

        # 循环选择列表
        for num in nums:
            # 已经加入路径的，就不要加啦
            if num in track:
                continue
            # 将这个选择加入路径
            # 从选择列表删除该选择
            track.append(num)
            # 迭代
            self.backtrack(track, nums)
            # 撤销选择
            # 将该选择重新加入选择列表
            track.pop()

def test_solution():
    result = Solution().permute([1,2,3])
    expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert len(result) == 6
    assert result == expected
    