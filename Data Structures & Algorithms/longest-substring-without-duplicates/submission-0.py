class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        state = {}
        max_length = 0

        while end in range(len(s)):
            state[s[end]] = state.get(s[end] , 0) + 1
            while state[s[end]] > 1:
                state[s[start]] -= 1
                start += 1
            max_length = max(max_length , end-start+1)
            end += 1


        return max_length



        