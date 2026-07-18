class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i , item in enumerate(nums):
            total = target - item
            if total in seen:
                return [seen[total], i]

            seen[item] = i
            
