class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindrome(i,j):
            while i<=j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        left = 0
        right = len(s)-1
        while left <= right:
            if s[left]!=s[right]:
                return palindrome(left+1,right) or palindrome(left,right-1)
            left+=1
            right-=1
        return True