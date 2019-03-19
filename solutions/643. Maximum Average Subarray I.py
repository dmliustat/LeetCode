class Solution:
    def findMaxAverage(self, nums, k):
        # Write your code here
        n = len(nums)
        sum = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            sum[i] = sum[i - 1] + nums[i - 1]
        ans = sum[k]
        for i in range(k + 1, n + 1):
            ans = max(ans, sum[i] - sum[i - k])
        return ans * 1.0 / k