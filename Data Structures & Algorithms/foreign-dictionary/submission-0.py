class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = {}
        for word in words:
            for ch in word:
                indegree[ch] = 0
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            for j in range(min(len(word1),len(word2))):
                if word1[j]!=word2[j]:
                    c1 = word1[j]
                    c2 = word2[j]
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2]+=1
                    break
        q = deque()
        for ch in indegree:
            if indegree[ch] == 0:
                q.append(ch)
        result = []
        while q:
            ch = q.popleft()
            result.append(ch)
            for adj in graph[ch]:
                indegree[adj]-=1
                if indegree[adj] == 0:
                    q.append(adj)
        if len(result)!=len(indegree):
            return ""
        return "".join(result)