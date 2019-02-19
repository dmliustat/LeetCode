class Solution:
    def findPeakElement(self, nums: 'List[int]') -> 'int':
        if ((len(nums) == 1) or ((len(nums) == 2) and (nums[0] > nums[1]))):
            return 0;
        if ((len(nums) == 2) and (nums[0] < nums[1])):
            return 1;
        start = 0
        end = len(nums) - 1
        if (nums[start+1] < nums[start]):
            return 0;
        if (nums[end-1] < nums[end]):
            return end;
        while start + 1 < end:
            mid = (end - start)//2 + start
            if ((nums[mid] > nums[mid-1]) and (nums[mid] > nums[mid+1])):
                return mid;
            elif (nums[mid] > nums[mid-1]):
                start= mid
            else:
                end = mid
        if (nums[start] < nums[end]):
            return end;
        else:
            return start;