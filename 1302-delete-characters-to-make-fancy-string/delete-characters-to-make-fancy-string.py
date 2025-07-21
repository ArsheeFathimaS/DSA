class Solution:
    def makeFancyString(self, s: str) -> str:
        res = s[:2]  # res = 'aa'
        for i in range(2, len(s)):
            if s[i] != res[-1] or s[i] != res[-2]:
                res += s[i]
        return res

        