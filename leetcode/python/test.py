def solution(nums, target):
    hash = {}
    for i, n in enumerate(nums):
        if hash.get(target-n):
            return [i, hash.get(target-n)]
        hash[n] = i

def solution2(node1, node2):
    