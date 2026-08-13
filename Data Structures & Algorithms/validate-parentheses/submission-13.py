class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {"[":"]","(":")","{":"}"}
        for string in s:
            if string in "[{(":
                stack.append(string)
            else:
                if not stack or string!=hashmap[stack[-1]]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0