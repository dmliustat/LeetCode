class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'int':
        if ((len(nums) == 0) or (not nums)):
            return -1;
        
        start = 0
        end = len(nums)-1
        
        while start + 1 < end:
            mid = (end - start)//2 + start
            if (nums[mid] > nums[end]):
                if (target == nums[end]):
                    return end;
                elif (target < nums[end]):
                    start = mid
                else:
                # (target > nums[end])
                    if (target == nums[mid]):
                        return mid;
                    elif (target < nums[mid]):
                        end = mid
                    else:
                        start = mid
            else:
            # nums[nums[mid] < nums[end]]
                if (target == nums[end]):
                    return end;
                elif (target < nums[end]):
                    if (target == nums[mid]):
                        return mid;
                    elif (target < nums[mid]):
                        end = mid
                    else:
                        start = mid
                else:
                # target > nums[end]
                    end = mid
            
        if (nums[start] == target):
            return start;
        elif (nums[end] == target):
            return end;
        else:
            return -1;