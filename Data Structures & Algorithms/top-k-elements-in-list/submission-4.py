class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [nums for nums,freq in Counter(nums).most_common(k)]
        