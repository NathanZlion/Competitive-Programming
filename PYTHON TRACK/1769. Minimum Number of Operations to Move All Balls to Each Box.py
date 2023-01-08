class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        answer = [0] * len(boxes)
        for i in range(len(boxes)):
            ans_at_i=0
            for j in range(len(boxes)):
                if i==j:
                    continue
                elif boxes[j]=='1':
                    ans_at_i += abs(j-i)
            answer[i] = ans_at_i

        return answer
