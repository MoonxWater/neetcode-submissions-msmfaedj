'''
make a cur_h to sum eating time
res will store the best answer

get max from the piles list
set low to 1 and high to max
while low <= high, run a loop
calc mid of low and high, floor div
run through the array and div each pile with mid and ceil it.
add the result to cur_h
if at anypoint cur_h exceeds h, break from inner loop
if break, koko too slow, increase speed: low to mid + 1
if did not break, koko either too
fast or perfect: high to mid - 1, res = mid
return res
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high

        while low <= high:
            mid = (low + high) // 2
            cur_h = 0

            for pile in piles:
                cur_h += math.ceil(pile / mid)

                if cur_h > h:
                    break
            else:
                res = mid
                high = mid - 1
                continue
            
            low = mid + 1

        return res