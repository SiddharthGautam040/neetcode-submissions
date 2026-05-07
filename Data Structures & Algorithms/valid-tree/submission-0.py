class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(n)}
        for edge, ver in edges:
            adjList[edge].append(ver)
            adjList[ver].append(edge)
        visit = set()
        
        def dfs(curr, prev):
            if curr in visit:
                return False
            
            visit.add(curr)

            for edge in adjList[curr]:
                if edge == prev:
                    continue
                if dfs(edge, curr) == False:
                    return False

            return True
            
        return dfs(0, None) and len(visit) == n
