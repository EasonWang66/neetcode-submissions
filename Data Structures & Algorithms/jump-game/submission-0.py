class Solution:
    def canJump(self, nums: List[int]) -> bool:
        best = 0
        for i in range(len(nums)):
            if i > best:
                return False
            best = max((i + nums[i]), best)
            if best >= len(nums) - 1:
                return True
        return False