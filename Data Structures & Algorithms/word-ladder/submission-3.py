class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # construct graph, if distance between words is 1 they area adj
        def distance(a,b):
            length = 0
            for i in range(len(a)):
                if a[i]!=b[i]:
                    length+=1
            return length
        wordList.append(beginWord)
        if endWord not in wordList:
            return 0
        graph = defaultdict(list)
        for i in range(len(wordList)-1):
            for j in range(i+1,len(wordList)):
                if distance(wordList[i],wordList[j])==1:
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
        q = deque()
        q.append(beginWord)
        visited = set()
        visited.add(beginWord)
        count = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return count
                for adj in graph[node]:
                    if adj not in visited:
                        visited.add(adj)
                        q.append(adj)
            count+=1
        return 0