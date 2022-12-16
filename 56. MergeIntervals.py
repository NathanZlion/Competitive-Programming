class Solution(object):
    def merge(self, intervals):
        def last(n):return n[0]
        def sort(listOfLists):return sorted(listOfLists, key=last)
        intervals = sort(intervals)
        res=[]
        ptr=0
        curr=intervals[ptr]
        while ptr < len(intervals):
            try:next = intervals[ptr+1]
            except:
                res.append(curr)
                break
            if curr[-1]>=next[0]:curr[-1]=max(next[-1], curr[-1])
            else:
                res.append(curr)
                curr=next
            ptr+=1
        return res
