class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort() # sorts candidates in place
        res = []

        def dfs(i, cur, total): # i is an index, cur is a list, total is an int
            if total == target:
                
                res.append(cur.copy())
                return 
            
            if i >= len(candidates) or total > target:
                return


            val = candidates[i]
            cur.append(candidates[i])
            dfs(i+1, cur, total + candidates[i]) # include element at candidate index i
            cur.pop()
            # we have to be clever to skip duplicates
            j = i +1
            while j < len(candidates) and candidates[j] == val:
                j += 1

            dfs(j, cur, total) 
        dfs(0,[],0)
        return res