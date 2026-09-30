class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high

        while low <= high:
            mid = (low + high) // 2

            time_taken = 0

            for pile in piles:
                time_taken += math.ceil(pile / mid)

                if time_taken > h:
                    low = mid + 1
                    break

            else:
                res = min(res, mid)
                high = mid - 1

        return res


        