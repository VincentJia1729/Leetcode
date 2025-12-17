# to solve this, you need to use Topological sort

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_req = {c: [] for c in range(numCourses)} # Python dictionary comprehension
        for crs, pre in prerequisites:
            pre_req[crs].append(pre)
        
        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True # this doesn't matter until you add to "visit"
                # when you confirm there is no cycle, you add to "visit"
            
            cycle.add(crs)
            for pre in pre_req[crs]:
                if dfs(pre) == False: # notice here we end up calling dfs() a bunch of times this is due to the call stack from recursion
                    return False # if dfs() == False once, then the whole thing is False    
            # once you break out (determine that there are no cycles)
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False: # if at any starting node, we find a cycle 
                # notice that dfs() is called a bunch of times here due to recursion call stack
                return [] 
        return output
