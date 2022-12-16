class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.list = []
        self.maxLength = k
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """

        if not self.isFull():
            self.list.insert(0,value)
            return True
        return False
        

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if not self.isFull():
            self.list.append(value)
            return True
        return False


    def deleteFront(self):
        """
        :rtype: bool
        """
        if not self.isEmpty():
            self.list.pop(0)
            return True
        return False  

    def deleteLast(self):
        """
        :rtype: bool
        """
        if not self.isEmpty():
            self.list.pop()
            return True
        return False

    def getFront(self):
        """
        :rtype: int
        """
        if not self.isEmpty():
            return self.list[0]
        return -1

    def getRear(self):
        """
        :rtype: int
        """
        if not self.isEmpty():
            return self.list[-1]
        return -1        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return len(self.list) == 0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.maxLength == len(self.list)
        
