class Solution:
    def check(self , piles: List[int] , mid: int , h: int) -> bool:
        hours = 0
        for i in range(len(piles)):

            hours += piles[i] // mid
            if piles[i] % mid != 0:
                hours += 1

        return hours<= h
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = 0
        low , high = 1 , max(piles)
        while low<=high:
            mid = low + (high - low)//2
            if self.check(piles , mid , h) == True:
                high = mid - 1
                res = mid
            else:
                low = mid + 1

        return res

        