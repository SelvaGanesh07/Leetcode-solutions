class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        c=0
        for ch in hours:
            if ch>=target:
                c+=1
        return c