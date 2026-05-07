class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        output = []
        visit, cycle = set(), set()
        preqMap = {i:[] for i in range(numCourses)}

        for crs, preq in prerequisites:
            preqMap[crs].append(preq)

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in preqMap[crs]:
                if dfs(pre) == False:
                    return False
                
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output