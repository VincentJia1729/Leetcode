class TrieNode:
    def __init__ (self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word:str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children: # not in the keys
                # create a new TrieNode and add it to the children of cur
                cur.children[c] = TrieNode()
            cur = cur.children[c] # move our pointer to the memory address of the TrieNode with key "c"
        cur.end_of_word = True # once you break out of the word, mark the TrieNode with "True"

        # if we have: cur.children['d'] = TrieNode()
        # then our dict looks like: { 'd': <new TrieNode object> }

    
    def search(self, word:str) -> bool:
        # this is honestly rly complicated
        # we need to cleverly use recursion

        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i] # go through the characters in word

                if c == ".":
                    for child in cur.children.values(): # cur.children.values() is the memory address for TrieNodes()
                        if dfs(i+1, child): # check for all possible children nodes of the current node
                            return True # if we find a match, in those  "subpaths" return True
                        # the idea is that we have a "normal travesral"
                        # and the "recursive" subproblem where we apply "normal traversal" on multiple paths
                    return False # if we don't find a valid subpath
                else:
                    if c not in cur.children: # if we hit a "dead end"
                        return False
                    cur = cur.children[c] # move cur to the child TrieNode
            return cur.end_of_word # we will break out at some point, see if that node is "flagged" with "end_of_word"

        return dfs(0, self.root) 





    