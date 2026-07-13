class Node:
    def __init__(self, val: int, key: int, prev: Optional[Node] = None, next: Optional[Node] = None):
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0, self.left)
        self.left.next = self.right

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]
        self._remove_node(node)
        self._insert_mru(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove_node(self.cache[key])
        
        self.cache[key] = Node(value, key)
        node = self.cache[key]
        self._insert_mru(node)
        
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self._remove_node(lru)
            self.cache.pop(lru.key)
            
    def _insert_mru(self, node: Node) -> None:
        prev = self.right.prev
        prev.next = node
        node.next = self.right
        node.prev = prev
        self.right.prev = node

    def _remove_node(self, node: Node) -> None:
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
