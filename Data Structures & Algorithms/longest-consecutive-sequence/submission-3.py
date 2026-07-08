class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums1 = sorted(set(nums))
        max_len = 1
        curr_len  = 1


        for i in range(1,len(nums1)):
            if nums1[i]  == nums1[i-1] + 1:
                curr_len += 1
                max_len = max(curr_len , max_len)
            else:
                curr_len = 1
        return max_len
            


        