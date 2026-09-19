class Solution:
    def longestPalindrome(self, s: str) -> str:
        # memoized solution
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
        start = 0
        max_len = 1
        for i in range(len(s)):
            for j in range(i,len(s)):
                if j-i+1<=max_len:
                    continue
                if rec(i,j):
                    max_len = max(j-i+1, max_len)
                    start = i
        return s[start:start+max_len]
