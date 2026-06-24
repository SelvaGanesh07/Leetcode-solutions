class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        c=0
        d=0
        for ch in nums:
            if ch<0:
               c+=1
            elif ch>0:
                d+=1
        return max(c,d) 