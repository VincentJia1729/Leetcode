class Node:
    def __init__(self, key, val): # called "val" by convention
        self.key, self.val = key, val
        self.prev = self.next = None # Python syntax (convenient)
        # this is just saying self.prev = None
        # and self.next = None




class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}

        # Left and Right pointers
        # Left pointer is the "least recently used"
        # Right pointer is the "most recently used"
        self.left = Node(0,0) # just have these be dummies with non-important intializations
        self.right = Node(0,0) 
        # then connect them together
        # why? This is to help avoid weird edge cases
        self.left.next=  self.right
        self.right.prev = self.left
        
    def remove(self,node):
        prev, nxt = node.prev, node.next # current prev and next of "node"
        prev.next  = nxt # move the pointers
        nxt.prev = prev

    # insert node into the front of list
    def insert(self, node):
        prev, nxt = self.right.prev , self.right
        # set old nodes to point to new node
        prev.next = node
        nxt.prev = node

        # set new node to point to old nodes
        node.next = nxt
        node.prev = prev

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache: # if we are in the dictionary
            self.remove(self.cache[key]) # remove the node
            self.insert(self.cache[key]) # then add it to the front
            return self.cache[key].val # returns the value of the node for "key:node" in dictionary 
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # if the key already exists, delete the old node
        # create a new node, and add it to the front of the double linked list
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value) # create a new Node
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next # least recently used is always the one to the right of the dummy left node
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)