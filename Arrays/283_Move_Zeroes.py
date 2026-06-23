class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z=[]
        n=[]
        for i in range(len(nums)):
            if nums[i]==0:
                z.append(0)
            else:
                n.append(nums[i])
        nums[:]=n+z