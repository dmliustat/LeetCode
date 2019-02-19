class Solution:
    def search(self, nums: 'List[int]', target: 'int') -> 'bool':
        if ((not nums) or (len(nums) == 0)):
            return False;
        start = 0
        end = len(nums) - 1
        while (start + 1 < end):
            mid = (end - start)//2 + start
            if (target == nums[end]):
                return True;
            elif (target > nums[end]):
                if (nums[mid] < nums[end]):
                    end = mid
                elif (nums[mid] > nums[end]):
                    if (nums[mid] == target):
                        return True;
                    elif (nums[mid] > target):
                        end = mid
                    else:
                        start = mid
                else:
                    if(nums[mid] == target):
                        return True;
                    else:
                        end = end - 1

            else:
                # target < nums[end]
                if (nums[mid] == nums[end]):
                    if (nums[mid] == target):
                        return True;
                    else:
                        end = end - 1
                elif (nums[mid] < nums[end]):
                    if (nums[mid] == target):
                        return True;
                    elif (nums[mid] < target):
                        start = mid
                    else:
                        end = mid
                else:
                    start = mid
        if ((nums[start] == target) or (nums[end] == target)):
            return True;
        else:
            return False;