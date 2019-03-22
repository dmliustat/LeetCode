class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend == 0):
            return 0;
        maxInt = 2147483647
        neg = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        ans, shift = 0, 31
        a, b = abs(dividend), abs(divisor)
        while shift >=0:
            if a >= b << shift:
                a -= b << shift
                ans += 1 << shift
            shift -= 1           
        if neg:
            ans = -ans
        if ans > 2147483647 or ans < -2147483648:
            return 2147483647
        return ans;
    