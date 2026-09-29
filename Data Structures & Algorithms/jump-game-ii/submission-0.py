class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        end = 0
        best = 0

        for i in range(len(nums) - 1):
            best = max(best, i + nums[i])

            if i == end:
                jumps += 1
                end = best

        return jumps