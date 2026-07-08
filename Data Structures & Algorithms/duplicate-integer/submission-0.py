from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = Counter(nums)
        print(s)
        for i in s:
            if s[i] > 1:
                return True
            
        return False
            
        