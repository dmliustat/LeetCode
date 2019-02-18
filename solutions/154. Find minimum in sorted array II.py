class Solution:
    def findMin(self, nums: 'List[int]') -> 'int':
        if ((not nums) or (len(nums)==0)):
            return -1;
        
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end:
            mid = (end - start)//2 + start
            target = nums[end]
            if (nums[mid] > target):
                start = mid
            elif (nums[mid] < target):
                end = mid
            else:
                end = end - 1  
        if (nums[start] < nums[end]):
            return nums[start];
        else:
            return nums[end];