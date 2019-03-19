class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        start = 1
        end = N
        while start < end:
            mid = (start + end)//2
            if self.f(mid, K, N) < N:
                start = mid + 1
            else:
                end = mid
        return start;
    
    def f(self, x, K, N):
        ans = 0
        r = 1
        for i in range(1, K+1):
            r *= x-i+1
            r //= i
            ans += r
            if ans >= N:
                break;
        return ans;
