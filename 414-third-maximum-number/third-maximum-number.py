class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        seen = set()
        for i in nums:
            if i not in seen:
                seen.add(i)
        my_list = list(seen)
        my_list.sort(reverse = True)
        if len(my_list)>=3:
            return my_list[2]
        return max(nums)
            