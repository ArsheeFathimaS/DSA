#User function Template for python3

class Solution:

    def findMinDiff(self, arr,M):
        min_diff = float('inf')
        arr.sort()
        for i in range(len(arr)-M+1):
            diff = arr[i+M-1] - arr[i]
            min_diff = min(diff, min_diff)
        return min_diff
            
        
            

       