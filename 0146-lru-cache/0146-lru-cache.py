
class Node:
    def __init__(self, key, value, prev = None, next_ = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next_


class DoublyLinkedList:
    def __init__(self):
        self.dummyHead = Node(-1, -1)
        self.dummyTail = Node(-1, -1)
        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead
        self._length = 0

    def popLastNode(self) -> Node:
        return self.popNode(self.dummyTail.prev)

    def popNode(self, node: Node) -> Node:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self._length -= 1
        return node

    def appendNode(self, newNode: Node) -> None:
        next_ = self.dummyHead.next
        self.dummyHead.next = newNode
        newNode.prev = self.dummyHead
        newNode.next = next_
        next_.prev = newNode
        self._length += 1

    def __len__(self):
        return self._length


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.doublyLinkedList = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.doublyLinkedList.popNode(node)
            self.doublyLinkedList.appendNode(node)
            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self.doublyLinkedList.popNode(node)
            self.doublyLinkedList.appendNode(node)
            node.value = value
        else:
            newNode = Node(key, value)
            self.map[key] = newNode
            self.doublyLinkedList.appendNode(newNode)

        if len(self.doublyLinkedList) > self.capacity:
            poppedNode = self.doublyLinkedList.popLastNode()
            del self.map[poppedNode.key]
            del poppedNode
