class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l, r = 0, 1
        max_uniq_char = len(set(s))
        window = set(s[l:r])
        max_len = 1

        while r < len(s):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            r += 1

            max_len = max(max_len, len(window))
            if max_len == max_uniq_char:
                return max_len

        return max_len