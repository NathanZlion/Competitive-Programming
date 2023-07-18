class Node:
    def __init__(self, key=-1, value=-1, prev=None, nxt=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = nxt

class DoublyLinkedList:
    """recent ones are at the tail, and least recent ones at the head."""
    def __init__(self):
        # Added 2 dummy Nodes at head and tail as a 
        # padding to simplify other implementations
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, node: Node):
        """push to the tail."""
        last_node = self.tail.prev
        last_node.next = node
        node.prev = last_node
        node.next = self.tail
        self.tail.prev = node

    def delete_node(self, node: Node) -> None:
        prevv = node.prev
        nextt = node.next
        prevv.next = nextt
        nextt.prev = prevv

    def make_recent(self, node: Node):
        """ 
        brings a least recent node next to the head 
        to the tail(more recent part)
        """
        self.delete_node(node)
        self.push(node)

    def evict_least_recent(self) -> Node:
        """delete the node next to the dummy head"""
        node_to_evict = self.head.next
        self.delete_node(node_to_evict)
        return node_to_evict

    def get_least_recent_node(self):
        return self.head.next

class LRUCache:
    def __init__(self, capacity: int):
        self.dll = DoublyLinkedList()
        self.capacity = capacity
        self.key_to_node = {}

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.dll.make_recent(node)

            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        # check if the node is in keys
        # if in keys delete that and also the node
        if key in self.key_to_node:
            node = self.key_to_node[key]
            del self.key_to_node[key]
            self.dll.delete_node(node)
        
        # add it to hash and dll
        new_node = Node(key, value)
        self.key_to_node[key] = new_node
        self.dll.push(new_node)

        # remove any excess node
        if len(self.key_to_node) > self.capacity:
            node_evicted = self.dll.evict_least_recent()
            del self.key_to_node[node_evicted.key]


