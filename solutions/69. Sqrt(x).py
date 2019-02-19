class Solution:
    def mySqrt(self, x: 'int') -> 'int':
        if (x == 0):
            return 0;
        if ((x == 1) or (x == 2)):
            return 1;
        start = 1
        end = x
        while start + 1 < end:
            mid = (end - start)//2 + start
            if ((mid*mid) < x):
                start = mid
            elif ((mid*mid) > x):
                end = mid
            else:
                return mid;
            
        return start;