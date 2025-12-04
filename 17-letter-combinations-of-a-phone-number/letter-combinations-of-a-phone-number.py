

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        result = [] # result will hold a list of lists
        combination = [] # this is a temp list to add to result

        num_to_alphabet = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
            }

        # i should start from 0
        # we need to apply a depth first search
        def dfs(i):

            if i == len(digits): # base case
                result.append("".join(combination.copy()))
                return 
            
            cur_num = digits[i]
            for c in num_to_alphabet[cur_num]:
                combination.append(c)
                dfs(i+1)
                combination.pop()

            
        dfs(0)
        return result
    

    