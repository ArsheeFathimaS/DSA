class Solution:
    def maxSubarraySum(self, arr):
        current = arr[0]
        maxx = arr[0]
        for i in range(1, len(arr)):
            current = max(arr[i], current + arr[i])
            maxx = max(current, maxx)
        return maxx
       
                
        
        
            