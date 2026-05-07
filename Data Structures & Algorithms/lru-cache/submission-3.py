class LRUCache:

    def __init__(self, capacity: int):
        self.left = Node()
        self.right = Node()
        self.cache = {}
        self.capacity = capacity
        self.curr_load = 0
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        # self.show_ll()
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            return

        if self.curr_load == self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            self.curr_load -= 1

        node = Node(key=key, val=value)
        self.insert(node)
        self.cache[key] = node
        self.curr_load += 1

    def insert(self, node):
        right = self.right
        left = right.prev
        left.next = node
        node.prev = left
        node.next = right
        right.prev = node

    def remove(self, node):
        prev = node.prev
        next_node = node.next
        prev.next = next_node
        next_node.prev = prev

    def show_ll(self):
        curr = self.left
        while curr:
            print(curr.key, end=" ")
            curr = curr.next
        print("")

class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev
