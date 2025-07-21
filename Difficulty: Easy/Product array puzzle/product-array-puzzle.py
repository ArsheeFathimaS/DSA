class Solution:
    def productExceptSelf(self, arr):
        prod = 1
        zero_count = arr.count(0)
        res = []

        if zero_count > 1:
            # More than one zero, every product will be zero
            return [0] * len(arr)
        
        for num in arr:
            if num != 0:
                prod *= num

        for num in arr:
            if zero_count == 0:
                res.append(prod // num)  # integer division to stay within 32-bit
            else:
                # Only one zero in array
                res.append(prod if num == 0 else 0)
        
        return res
