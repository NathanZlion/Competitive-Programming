class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        left = 0
        right = len(cardPoints)- k
        maxSum = sum(cardPoints[right:])
        result = maxSum

        while right < len(cardPoints):
            maxSum += cardPoints[left]
            maxSum -= cardPoints[right]
            left +=1
            right +=1
            result = max(result, maxSum)
        
        return result


