class Solution:
    def isValid(self, word: str) -> bool:
        letters ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        cons = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
        vowels = "aeiouAEIOU"
        digits = "1234567890"
        char = 0
        vowel_count = 0
        cons_count = 0
        for i in word:
            if i not in letters and i not in digits:
                return False
            if i in letters or i in digits:
                char+=1
            if i in vowels:
                vowel_count+=1
            if i in cons:
                cons_count+=1
        if char>=3 and vowel_count>=1 and cons_count>=1:
            return True
        return False
        