class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # building adjList and prerequisitedCount from the given prerequisites
        adjList = defaultdict(list)
        prerequisitedCount = defaultdict(int)

        for requiredCourse, nextCourse in prerequisites:
            prerequisitedCount[nextCourse] += 1
            adjList[requiredCourse]. append(nextCourse)
        
        # Initialize the learning queue for courses with no prerequsites.
        learningQueue = deque()

        for course in range(numCourses):
            if not prerequisitedCount[course]:
                learningQueue.append(course)
        
        numCompletedCourses = 0

        while learningQueue:
            currCourse = learningQueue.popleft()
            numCompletedCourses += 1

            # Decrement priority count for courses that have currCourse as a prerequisite
            for nextCourse in adjList[currCourse]:
                prerequisitedCount[nextCourse] -= 1

                if not prerequisitedCount[nextCourse]:
                    learningQueue.append(nextCourse)

        # checks if all courses have been completed
        return numCompletedCourses == numCourses
