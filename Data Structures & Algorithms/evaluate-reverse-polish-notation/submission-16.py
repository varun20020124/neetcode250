class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def compute(x, y, op):
            if op == "+":
                return y + x
            elif op == "-":
                return y - x
            elif op == "*":
                return y * x
            else:
                return int(y / x)

        stack = []
        operators = ["+","-","*","/"]
        for char in tokens:
            if char not in operators:
                stack.append(int(char))
            else:
                x = stack.pop()
                y = stack.pop()
                stack.append(compute(x,y,char))
        return stack[0]