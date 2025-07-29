class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        counter = Counter(arr)
        max_lucky = -1
        for num in counter:
            if num == counter[num]:
                max_lucky = max(max_lucky, num)
        return max_lucky
    

        

        