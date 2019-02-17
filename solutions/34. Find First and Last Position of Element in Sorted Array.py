class Solution:
    def searchRange(self, nums: 'List[int]', target: 'int') -> 'List[int]':  
        if ((len(nums) == 0) or (not nums)):
            return [-1, -1];
        
        # find the first position
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (end - start)//2 + start
            if (nums[mid] < target):
                start = mid
            elif (nums[mid] == target):
                end = mid
            else:
                end = mid
        if (nums[start] == target):
            first = start
        elif (nums[end] == target):
            first = end
        else:
            first = -1
            last = -1
        
        if (first != -1):
            # find the last position        
            start = 0
            end = len(nums) - 1
            while start + 1 < end:
                mid = (end - start)//2 + start
                if (nums[mid] < target):
                    start = mid
                elif (nums[mid] == target):
                    start = mid
                else:
                    end = mid
            if (nums[end] == target):
                last = end
            else:
                last = start
            
        return [first, last];
                