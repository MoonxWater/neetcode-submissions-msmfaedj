class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        l = r = 0
        max_len = 0
        seen = set()

        while r < len(s):
            if s[r] in seen:
                max_len = max(max_len, len(seen))
                seen.remove(s[l])
                l += 1
            else:
                seen.add(s[r])
                r += 1

        return max(max_len, len(seen))
