class Solution:
    def peakIndexInMountainArray(self, A: 'List[int]') -> 'int':
        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = (end - start)//2 + start
            if (A[mid] < A[mid-1]):
                end = mid
            else:
                start = mid
        if (A[start] > A[end]):
            return start
        else:
            return end