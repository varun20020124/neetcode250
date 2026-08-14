class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        data = path.split("/")
        for i in range(len(data)):
            char = data[i]
            if char == "" or char == ".":
                continue
            elif char == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return "/" + "/".join(stack)