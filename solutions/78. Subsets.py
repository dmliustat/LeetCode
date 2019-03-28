class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        if (nums == None or len(nums) == 0):
            return result;
        self.dfs(nums, 0, [], result)
        return result;

    def dfs(self, nums, index, combination, result):
        result.append(list(combination))

        for i in range(index, len(nums)):
            combination.append(nums[i])
            self.dfs(nums, i+1, combination, result)
            combination.pop()