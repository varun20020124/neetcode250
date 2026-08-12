class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # [1,2,2,3,3]
        people.sort()
        i = 0
        j = len(people)-1
        boats = 0
        while i<=j:
            total = people[i]+people[j]
            if total > limit:
                boats+=1
                j-=1
            else:
                boats+=1
                i+=1
                j-=1
        return boats