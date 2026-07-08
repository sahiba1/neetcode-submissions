from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums1 = Counter(nums)
        li = []
        while k!=0:
            target_value = max(nums1.values())
            matching_key = [key for key, value in nums1.items() if value == target_value]
            for key in matching_key:
                li.append(key)
                del nums1[key]
                k = k - 1

        return li

        