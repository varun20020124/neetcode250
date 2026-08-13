class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op not in ["+","D","C"]:
                record.append(int(op))
            if op == "+":
                x = record[-1]
                y = record[-2]
                record.append(x+y)
            if op == "D":
                record.append(record[-1] * 2)
            if op == "C":
                record.pop()
        return sum(record)