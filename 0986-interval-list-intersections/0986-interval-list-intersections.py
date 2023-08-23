class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        def doIntersect(interval1: List[int], interval2: List[int]) -> bool:
            start1, end1 = interval1
            start2, end2 = interval2
            return not (start1 > end2 or start2 > end1)

        def intersection(interval1: List[int], interval2: List[int]) -> List[int]:
            start1, end1 = interval1
            start2, end2 = interval2
            
            return [max(start1, start2), min(end1, end2)]
        
        ptr1 = ptr2 = 0
        n,m = len(firstList), len(secondList)
        res = []

        while ptr1<n and ptr2<m:
            interval1, interval2 = firstList[ptr1], secondList[ptr2]

            if doIntersect(interval1, interval2):
                res.append(intersection(interval1, interval2))

            if interval1[1] > interval2[1]:
                ptr2 += 1
            else:
                ptr1 += 1
        
        return res