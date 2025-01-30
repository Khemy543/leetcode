class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev, self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map keys to nodes

        # create least and most recently used nodes
        # left = LRU, right = MRU
        self.left, self.right = Node(0,0), Node(0,0)
        # connect the two nodes
        self.left.next, self.right.prev = self.right, self.left

    # remove from linkedlist
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        
    # insert at right most position of linked list
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.next = self.right
        self.right.prev = node
        node.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            # update the most recent node (mlu)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove node
            self.remove(self.cache[key])
            # create a new Node and insert
            self.cache[key] = Node(key, value)
            # insert into our list
            self.insert(self.cache[key])

            if len(self.cache) > self.capacity:
                # remove lru and update lru
                lru = self.left.next
                self.remove(lru)
                del self.cache[lru.key]