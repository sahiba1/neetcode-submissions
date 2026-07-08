from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        result = []

        if zero_count > 1:
            # More than one zero: all products will be zero
            return [0] * len(nums)

        total_product = 1
        for num in nums:
            if num != 0:
                total_product *= num

        for num in nums:
            if zero_count == 0:
                result.append(total_product // num)
            else:
                # Only one zero: product is non-zero only at the zero's index
                result.append(total_product if num == 0 else 0)

        return result
