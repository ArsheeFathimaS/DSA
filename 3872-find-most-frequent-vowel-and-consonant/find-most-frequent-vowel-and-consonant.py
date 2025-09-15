from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set("aeiou")
        c = Counter(s)
        max_vowels = 0
        max_consonants = 0

        for ch, count in c.items():
            if ch.isalpha():
                if ch in vowels:
                    max_vowels = max(max_vowels, count)
                else:
                    max_consonants = max(max_consonants, count)
        return max_vowels + max_consonants

        