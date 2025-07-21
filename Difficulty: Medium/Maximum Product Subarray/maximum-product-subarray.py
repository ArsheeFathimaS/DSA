class Solution:
	def maxProduct(self,arr):
	    min_prod = max_prod = res = arr[0]
	    for i in range(1, len(arr)):
	        num = arr[i]
	        if num<0:
	            min_prod, max_prod = max_prod, min_prod
	        min_prod = min(num, min_prod*num)
	        max_prod = max(num, max_prod*num)
	        res = max(max_prod, res)
	    return res
	    