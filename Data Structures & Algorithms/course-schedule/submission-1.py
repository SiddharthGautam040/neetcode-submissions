class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:[] for i in range(numCourses) }

        for prerequisite in prerequisites:
            preMap[prerequisite[0]].append(prerequisite[1])

        visited = set()
        def dfs(crs):
            if preMap[crs] == []:
                return True
            
            if crs in visited:
                return False
            visited.add(crs)

            can_done = True
            for pre in preMap[crs]:
                can_done = can_done and dfs(pre)

            if not can_done:
                return False
            visited.remove(crs)
            return True


        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        return True
