class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i: [] for i in range(numCourses)} # dictinoary comprehension in Python
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        visited = set() # to keep track if we have a cycle
        # we have a cycle if we visit an element in visited more than once

        def dfs(crs): # remember that crs has pre. Course has Prerequisite
            if crs in visited:
                return False
            if pre_map[crs] == []:
                return True
            
            visited.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre): # dfs(pre) evaluates to False when we have a cycle
                    # so, if we have a cycle in any course
                    return False # because then we cannot complete the course cycle
            
            visited.remove(crs)
            pre_map[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False # if for any node, we have dfs(crs) = False (have a cycle), then not dfs(crs) will be True. Thus, we return False for the whole function
        return True # if no errors, then we break out and return True



