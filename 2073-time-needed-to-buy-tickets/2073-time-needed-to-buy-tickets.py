class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        line_length = len(tickets)
        tickets = deque(tickets)

        while tickets[k]:
            if tickets[0]:
                tickets.append(tickets.popleft()-1)
                time += 1
            else:
                tickets.append(tickets.popleft())
            
            k = (k-1)%line_length
        
        return time

                
            