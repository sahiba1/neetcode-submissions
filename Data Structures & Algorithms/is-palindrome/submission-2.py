class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        if cleaned[::-1] == cleaned:
            return True
        else:
            return False
        