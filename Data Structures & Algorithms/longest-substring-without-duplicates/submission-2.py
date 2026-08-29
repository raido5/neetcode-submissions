class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        l = 0
        r = 0
        count = 0

        while r < len(s):
            if s[r] not in ss:
                ss.add(s[r])
                count = max(count, r - l + 1)
                r += 1
            else:
                ss.remove(s[l])
                l += 1

        return count