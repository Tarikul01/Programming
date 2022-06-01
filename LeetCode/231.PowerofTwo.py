class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        pow = 1
        if n == 1:
            return True
        else:
            while pow < n:
                pow = pow * 2
            return n == pow
solve=Solution()
print(solve.isPowerOfTwo(6))