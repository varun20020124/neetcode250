class Solution:
    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s
        return string
        
    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        result = []
        while j < len(s):
            while s[j]!="#":
                j+=1
            length = int(s[i:j])
            j+=1
            i = j
            j = length + i
            result.append(s[i:j])
            i = j
        return result