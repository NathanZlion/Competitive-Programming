class MinStack(object):

    def __init__(self):
        self.list = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.list.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        return self.list.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.list[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.list)
        
