"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # convert to adjecency list
        adjList : Dict[Tuple[int, int]]= {}
        importance : Dict[int, int] = {}
        discovered : Set[int] = set()

        for employee in employees:
            adjList[employee.id] = (employee.importance, employee.subordinates)
            importance[employee.id] = 0


        def discover(employee: int):
            nonlocal importance
            nonlocal discovered
            
            currImportance, currSubordinates = adjList[employee]
            
            if employee in discovered: return importance[employee]

            discovered.add(employee)
            importance[employee] += currImportance

            for subordinate in currSubordinates:
                importance[employee] += discover(subordinate)

            return importance[employee]


        for employee in employees:
            if not employee.id in discovered:
                discover(employee.id)

        return importance[id]

