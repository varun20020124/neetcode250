class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        data = path.split("/")
        for i in range(len(data)):
            char = data[i]
            if char == "..":
                if stack:
                    stack.pop()
            elif char!="" and char != ".":
                stack.append(char)
        return "/" + "/".join(stack)