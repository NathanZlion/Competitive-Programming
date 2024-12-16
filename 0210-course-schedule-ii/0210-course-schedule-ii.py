class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        numPrerequisites = {course: 0 for course in range(numCourses)}
        childList = {course: [] for course in range(numCourses)}
        
        for courseA, courseB in prerequisites:
            numPrerequisites[courseA] += 1
            childList[courseB].append(courseA)
        
        queue = deque()
        
        for course in range(numCourses):
            if numPrerequisites[course] == 0:
                queue.append(course)
        
        res = []
        
        while queue:
            course = queue.popleft()
            res.append(course)
            
            for childCourse in childList[course]:
                numPrerequisites[childCourse] -= 1
                if numPrerequisites[childCourse] == 0:
                    queue.append(childCourse)
        
        return res if len(res) == numCourses else []
