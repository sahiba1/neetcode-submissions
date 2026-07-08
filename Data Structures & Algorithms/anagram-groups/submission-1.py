
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        d = defaultdict(list)
        for i in strs:
            key = ''.join(sorted(i))
            d[key].append(i)
        return list(d.values())


       


        