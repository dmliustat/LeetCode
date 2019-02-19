class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if ((not L) or (len(L) == 0)):
            return 0;
        if (len(L) == 1):
            return L//k;
        
        start = 1
        end = sum(L)//k
        if (end == 0):
            return 0;
        while start+1 < end:
            mid = (end - start)//2 + start
            temp = sum([(x//mid) for x in L])
            if (temp >= k):
                start = mid
            else:
                end = mid

        temp = sum([(x//end) for x in L])
        if temp>=k:
            return end;
        temp = sum([(x//start) for x in L])
        if (temp>=k):
            return start;
        else:
            return 0;