class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        minimum = math.inf
        while l<=r:
            rate = (l+r)//2
            time = 0
            for pile in piles:
                time+=math.ceil(pile/rate)
            if time <= h:
                r = rate - 1
                minimum = min(minimum,rate)
            else:
                l = rate + 1
        return minimum