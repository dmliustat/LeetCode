 def countCopiers(pages, p):
        # p must be greater than all pages[i]
        n = 0
        page_sum = 0
        for i in range(len(pages)):
            page_sum = page_sum + pages[i]
            if (page_sum == p):
                n = n + 1
                page_sum = 0
            elif (page_sum > p):
                n = n + 1
                page_sum = pages[i]
            
        if (page_sum == 0):
            return n;
        else:
            return (n + 1);

class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        if ((not pages) or (len(pages) == 0)):
            return 0;
        if (len(pages) <= k):
            return max(pages);
            
        start = max(pages)
        end = sum(pages)
        while (start + 1 < end):
            mid = (end - start)//2 + start
            if (countCopiers(pages, mid) > k):
                start = mid
            else:
                end = mid
        if (countCopiers(pages, start) <= k):
            return start;
        else:
            return end;
            