class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:      
        left =1
        right = max(piles)
        result = right

        while left <= right:
            k = (right + left) // 2

            hours = sum(math.ceil(p / k) for p in piles)

            if hours <= h:

                result = k
                right = k - 1
            else:
                left = k + 1

        return result