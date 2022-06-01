class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        pow = 1
        if n == 1:
            return True
        else:
            while pow < n:
                pow = pow * 3
            return n == pow
