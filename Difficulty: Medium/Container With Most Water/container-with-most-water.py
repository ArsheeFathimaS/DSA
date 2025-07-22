
class Solution:
    def maxWater(self, arr):
        i = 0
        j = len(arr)-1
        max_water = 0
        
        while i<j:
            height = min(arr[i], arr[j])
            width = j-i
            area = height*width
            max_water = max(area, max_water)
            
            if arr[i]<arr[j]:
                i+=1
            else:
                j-=1
            
        return max_water
        
                    
        