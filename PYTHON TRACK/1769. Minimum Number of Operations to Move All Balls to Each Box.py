class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        answer = [0] * len(boxes)
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if i==j:
                    continue
                elif boxes[j]=='1':
                    answer[i] += abs(j-i)
        
        return answer
