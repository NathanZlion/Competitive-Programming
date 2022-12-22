class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        total = 0
        minimum = 1000000
        maximum = 1000

        for pay in salary:
            if (pay < minimum):
                minimum = pay

            if (pay > maximum):
                maximum = pay
        
        for pay in salary:
            if (pay not in {minimum, maximum}):
                total += pay
        
        average = float(total)/float(len(salary)-2)
        return average
