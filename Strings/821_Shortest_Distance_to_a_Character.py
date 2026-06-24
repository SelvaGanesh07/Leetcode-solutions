class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result = []
        for i in range(len(s)):
            min_dist = len(s)
            for j in range(len(s)):
                if s[j] == c:
                    min_dist = min(min_dist, abs(i - j))
            result.append(min_dist)
        return result