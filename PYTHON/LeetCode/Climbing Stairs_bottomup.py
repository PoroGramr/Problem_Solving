data = { 1 : 1, 2: 2, 3: 3}
class Solution: 
    def climbStairs(self, n: int) -> int:
        for i in range(3,46):
            data[i] = data[i-1] + data[i-2]
        return data[n]
