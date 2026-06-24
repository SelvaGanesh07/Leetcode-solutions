class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        m=n*(n+1)//2
        return m-sum(nums)