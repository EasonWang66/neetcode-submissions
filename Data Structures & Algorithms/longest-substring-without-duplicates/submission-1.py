class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left = 0
        best = 0

        for right in range(len(s)):

            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
                
            charSet.add(s[right])

            best = max(best, right - left +1)

        return best


            