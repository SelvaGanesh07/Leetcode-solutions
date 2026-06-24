class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for ch in set(nums):
            if nums.count(ch)>len(nums)//2:
                return ch