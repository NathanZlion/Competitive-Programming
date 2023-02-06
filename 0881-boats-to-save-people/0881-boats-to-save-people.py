class Solution(object):
    def numRescueBoats(self, people, limit):
        
        people.sort()

        boats = []

        ptr1 = 0
        ptr2 = len(people)-1
        
        while ptr1 < ptr2:
            if people[ptr1] + people[ptr2] > limit:
                boats.append(people[ptr2])
            else:
                boats.append(people[ptr1] + people[ptr2])
                ptr1 += 1
            ptr2 -= 1
        
        if ptr1 == ptr2:
            return len(boats) +1

        return len(boats)
