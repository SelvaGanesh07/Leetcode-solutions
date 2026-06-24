class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=list(set(nums1))
        b=list(set(nums2))
        c=[]
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i]==b[j]:
                    c.append(a[i])
        return c