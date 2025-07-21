class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = nums.count(0)
        res = []

        if zero_count > 1:
            # More than one zero, every product will be zero
            return [0] * len(nums)
        
        for num in nums:
            if num != 0:
                prod *= num

        for num in nums:
            if zero_count == 0:
                res.append(prod // num)  
            else:
                # Only one zero in array
                res.append(prod if num == 0 else 0)
        
        return res
        