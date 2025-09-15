class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        arr = text.split()
        for i in text.split():
            for j in brokenLetters:
                if j in i:
                    arr.remove(i)
                    break
        return len(arr)
            
        