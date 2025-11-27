class TrieNode:
    def __init__ (self):
        # default settings for a TrieNode
        self.children = {} # this dict for "self.children" will only contain lowercase letters "a-z"
        self.end_of_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode() # root is an empty TrieNode

    def insert(self, word: str) -> None:
        cur = self.root # start at root

        for c in word:
            if c not in cur.children: # cur.children is a dict, check if "c" is a key in "cur.children"
                cur.children[c] = TrieNode()
            cur = cur.children[c] # move pointer to new TrieNode
        cur.end_of_word = True # set the last node of the word to have "end_of_word" to be "True"
        # example. if "word = apple" then you would set the TrieNode containing "e" to have "end_of_node = True"

    def search(self, word: str) -> bool:
        cur = self.root # start at root

        for c in word:
            if c not in cur.children: # if you cannot find the next needed letter
                return False
            cur = cur.children[c]
        return cur.end_of_word # if you get to the end of the word, see if we marked it with a "True" flag

    def startsWith(self, prefix: str) -> bool:
        cur = self.root 

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True # if you can make it through the letters in prefix, then the prefix must exist 

