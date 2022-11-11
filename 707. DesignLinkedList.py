class MyLinkedList(object):

    def __init__(self):
        self.LinkedList = []

    def get(self, index):
        try:return self.LinkedList[index]
        except:
            return -1

    def addAtHead(self, val):
        self.LinkedList.insert(0,val)
        

    def addAtTail(self, val):
        self.LinkedList.append(val)


    def addAtIndex(self, index, val):
        if index <= len(self.LinkedList):    
            self.LinkedList.insert(index, val)
        else:
            pass
        

    def deleteAtIndex(self, index):
        try:self.LinkedList.pop(index)
        except:
            pass
