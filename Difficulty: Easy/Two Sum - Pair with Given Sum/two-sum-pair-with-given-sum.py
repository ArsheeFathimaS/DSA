class Solution:
    def twoSum(self, arr, target):
        arr.sort()
        n = len(arr)
        l, r = 0, n - 1
        
        while l < r:
            s = arr[l] + arr[r]
            if s == target:
                return True
            elif s < target:
                l += 1
            else:
                r -= 1
        return False

      
		          
		  
		  
		  