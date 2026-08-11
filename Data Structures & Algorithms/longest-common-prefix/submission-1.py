class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = math.inf
        word = None
        for string in strs:
            if len(string) < min_length:
                min_length = len(string)
                word = string
        lcp = []
        for i in range(min_length):
            letter = word[i]
            for string in strs:
                if letter != string[i]:
                    return "".join(lcp)
            lcp.append(letter)
        return "".join(lcp)