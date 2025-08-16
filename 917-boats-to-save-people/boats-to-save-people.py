class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        l = 0
        r = n-1
        total_time = 0
        while l<r:
            if people[l]+people[r] <= limit:
                l+=1
                r-=1
            else:
                r-=1
            total_time+=1
        if l==r:
            total_time+=1
        return total_time


            

        