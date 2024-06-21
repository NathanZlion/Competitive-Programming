class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        running_satisfied_customers = 0

        for i in range(n):
            running_satisfied_customers += ((1 - grumpy[i]) * customers[i])

        for i in range(minutes):
            if grumpy[i] == 1: # is grumpy
                running_satisfied_customers += customers[i]
        
        max_satisfied_customers = running_satisfied_customers
        for i in range(minutes, n):
            if grumpy[i] == 1:
                running_satisfied_customers += customers[i]

            if grumpy[i - minutes] == 1:
                running_satisfied_customers -= customers[i - minutes]
            
            max_satisfied_customers = max(max_satisfied_customers, running_satisfied_customers)
        
        return max_satisfied_customers
