from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)

        for s in s_count:
            if s_count[s] != t_count[s]:
                return False
        for t in t_count:
            if t_count[t] != s_count[t]:
                return False
        return True
                

        