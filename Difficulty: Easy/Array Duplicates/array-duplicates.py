class Solution:
    def findDuplicates(self, arr):
        seen = set()
        duplicates = set()
        for element in arr:
            if element in seen:
                duplicates.add(element)
            else:
                seen.add(element)
        return sorted(list(duplicates))
        
        