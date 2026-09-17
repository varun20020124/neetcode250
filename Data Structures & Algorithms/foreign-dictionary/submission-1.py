class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # build graph
        graph = defaultdict(set)
        visited = set()
        for word in words:
            for ch in word:
                visited.add(ch)
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            length = min(len(word1),len(word2))
            for j in range(length):
                if word1[j]!=word2[j]:
                    graph[word1[j]].add(word2[j])
                    break
        # build indegree
        indegree = {ch : 0 for ch in visited}
        for node in graph:
            for adj in graph[node]:
                indegree[adj]+=1
        # topological sort 
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
        if len(visited)!=len(result):
            return ""
        return "".join(result)
