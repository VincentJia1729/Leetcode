# This is the function we want to change

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.count_pali(s, i, i) # for odd length palidromes
            res += self.count_pali(s, i , i+1) # for even length palindrome
        return res

    def count_pali(self, s, l , r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res
