class Solution:
    def numRescueBoats(self, people, limit):
        people.sort()
        boats = []

       # if fattest person can't ever go with the thinnest person he should go alone
        while len(people) > 0 and people[len(people)-1] > (limit - people[0]):
            boats.append(people[-1])
            people.pop()
 

        index2 = len(people) - 1
            
        while 0 < index2:
            if (people[0] + people[index2]) == limit:
                boats.append(limit)
                people.pop(index2)
                people.pop(0)
                index2 = len(people) - 1
            elif (people[0] + people[index2]) > limit:
                index2 -=1
            else:
                boats.append(people[0] + people[index2])
                people.pop(index2)
                people.pop(0)
                index2 = len(people) - 1
              

        last = []   # remaining people from the above
        amountOfPassangers = []  # this is intended to limit the number of passanger aboard to 2
        for weight in people:
            added = False
            for index in range(len(last)):
                if (limit - last[index] >= weight) and (amountOfPassangers[index] < 2):
                    last[index] += weight
                    added = True
                    amountOfPassangers[index] +=1

            if not added:
                last.append(weight)
                amountOfPassangers.append(1)

        return (len(boats) + len(last))
