class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=0
        for ch in accounts:
            m=max(m,sum(ch))
        return m