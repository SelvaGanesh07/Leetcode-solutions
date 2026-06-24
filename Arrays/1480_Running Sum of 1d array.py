class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s=0
        l=[]
        for ch in nums:
            s=s+ch
            l.append(s)
        return l