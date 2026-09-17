class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src,dest in sorted(tickets)[::-1]:
            graph[src].append(dest)
        stack = []
        stack.append("JFK")
        result = []
        while stack:
            curr = stack[-1]
            if not graph[curr]:
                result.append(stack.pop())
            else:
                stack.append(graph[curr].pop())
        return result[::-1]