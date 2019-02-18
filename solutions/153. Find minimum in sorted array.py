class Solution:
    def findMin(self, nums: 'List[int]') -> 'int':
        if ((not nums) or (len(nums)==0)):
            return -1;
        
        target = nums[len(nums) - 1]
        start =0
        end = len(nums) - 1
        
        while start + 1 < end:
            mid = (end - start)//2 + start
            if (nums[mid] > target):
                start = mid
            else:
                end = mid
        if (nums[start] <= target):
            return nums[start];
        else:
            return nums[end];