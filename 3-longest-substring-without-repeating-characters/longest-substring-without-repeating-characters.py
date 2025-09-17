class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_max = 0
        max_streak = 0
        seen = []

        for i in s:
            if i not in seen:
                seen.append(i)
                curr_max += 1
                max_streak = max(max_streak, curr_max)
            else:
                dup_index = seen.index(i)
                seen = seen[dup_index + 1:] + [i]
                curr_max = len(seen)
                max_streak = max(max_streak, curr_max)

        return max_streak
