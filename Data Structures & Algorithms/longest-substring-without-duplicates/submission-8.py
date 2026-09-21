class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        seen = {}
        l = 0
        max_len = 1
        max_uniq_char = len(set(s))

        for r, char in enumerate(s):
            if char in seen:
                l = max(l, seen[char] + 1)
            seen[char] = r
            max_len = max(max_len, r - l + 1)
            if max_len == max_uniq_char:
                return max_len

        return max_len