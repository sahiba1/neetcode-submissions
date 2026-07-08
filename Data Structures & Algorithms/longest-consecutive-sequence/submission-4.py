class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 1
        curr_len = 1
        if len(nums) == 0:
            return 0
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                curr_len += 1
            
            elif nums[i] == nums[i - 1]:
                continue

            else:
                curr_len = 1
            max_len = max(max_len , curr_len)
            
        return max_len
            


        