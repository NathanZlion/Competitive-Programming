class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        for index, (enqueueTime, processingTime) in enumerate(tasks):
            tasks[index] = (enqueueTime, processingTime, index)

        heapify(tasks)

        availableTasks : List[Tuple(int, int)] = []        # [(processingTime, index), ...]
        timer = 0                                          # the current time
        executionOrder = []                                # the order in which the cpu chooses to execute tasks


        def execute():
            """choose task with shortest processing time from available tasks and execute it"""
            nonlocal timer

            processingTime, index = heappop(availableTasks)
            executionOrder.append(index)
            timer += processingTime


        def dispatch():
            """
            adds to `availableTasks` those tasks whose `enqueueTime` is within the `timer`, current time.
            If none exist as such, I just add the one with least `enqueueTime` and move the timer to that time.
            """
            nonlocal timer

            while tasks and timer >= tasks[0][0]:
                enqueueTime, processingTime, index = heappop(tasks)
                heappush(availableTasks, (processingTime, index))

            if not availableTasks:
                enqueueTime, processingTime, index = heappop(tasks)
                heappush(availableTasks, (processingTime, index))
                timer = enqueueTime


        while availableTasks or tasks:
            dispatch()
            execute()


        return executionOrder
