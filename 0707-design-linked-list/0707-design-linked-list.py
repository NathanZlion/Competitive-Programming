    
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        curr = self.head
        
        for _ in range(index):
            curr = curr.next
        
        return curr.val


    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        
        newNode = Node(val)

        if index == 0 or not self.head:
            newNode.next = self.head
            self.head = newNode
            self.length += 1
            return

        curr = self.head
        for _ in range(index-1):
            curr = curr.next
        
        nextNode = curr.next
        curr.next = newNode
        newNode.next = nextNode
        self.length += 1


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return

        dummyNode = Node(-1)
        dummyNode.next = self.head
        
        curr = dummyNode
        for _ in range(index):
            curr = curr.next
        
        curr.next = curr.next.next
        self.head = dummyNode.next
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)