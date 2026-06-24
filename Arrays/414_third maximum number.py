class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m=list(set(nums))
        n=len(m)
        m.sort(reverse=True)
        if n>=3:
            return m[2]
        else:
            return m[0]