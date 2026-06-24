class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=''
        for ch in s:
            if ch.isalnum():
                r+=ch.lower()
        return r==r[::-1]