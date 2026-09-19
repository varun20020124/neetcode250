class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = [[None] * len(s) for _ in range(len(s))]
        def rec(i,j):
            if i>=j:
                return True
            if memo[i][j]!=None:
                return memo[i][j]
            if s[i]!=s[j]:
                memo[i][j] = False
            else:
                memo[i][j] = rec(i+1,j-1)
            return memo[i][j]
        count = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if rec(i,j):
                    count+=1
        return count