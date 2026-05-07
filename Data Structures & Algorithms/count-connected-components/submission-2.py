class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        adjList = {i:[] for i in range(n)}
        for edge, ver in edges:
            adjList[edge].append(ver)
            adjList[ver].append(edge)
        visit = set()
        def dfs(curr, prev):
            if curr in visit:
                return 0
            
            visit.add(curr)

            for edge in adjList[curr]:
                if edge == prev:
                    continue
                dfs(edge, curr)

            return 1
            
        for i in range(n):
            if i not in visit:
                res = res + 1
                dfs(i, None) 
        return res