class MyQueue(object):

    def __init__(self):
        self.list = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.list.append(x)

    def pop(self):
        """
        :rtype: int
        """
        return self.list.pop(0)
        

    def peek(self):
        """
        :rtype: int
        """
        return self.list[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.list) == 0
