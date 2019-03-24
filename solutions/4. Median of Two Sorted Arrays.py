class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = len(nums1), len(nums2)
        if a > b:
            nums1, nums2, a, b = nums2, nums1, b, a
        
        imin, imax, length = 0, a, (a + b + 1) // 2
        while imin <= imax:
            flag = 0
            i = (imin + imax) // 2
            j = length - i
            
            if  i < a:
            # i < a is equivalent to j > 0
                if nums2[j-1] > nums1[i]:
                    # i is too small, increase i
                    imin = i + 1
                    flag = 1
                    
            if i > 0 and flag == 0:
            # i > 0 is equivalent to j < n
                if nums2[j] < nums1[i-1]:
                    # i is too large, decrese i
                    imax = i - 1
                    flag = 1
                    
            if flag == 0:
                # i is found
                if i == 0:
                    LeftMax = nums2[j-1]
                elif j == 0:
                    LeftMax = nums1[i-1]
                else:
                    LeftMax = max(nums1[i-1], nums2[j-1])
                    
                if (a + b) % 2 == 1:
                    return LeftMax * 1.0;
                else:
                    if i == a:
                        RightMin = nums2[j]
                    elif j == b:
                        RightMin = nums1[i]
                    else:
                        RightMin = min(nums1[i], nums2[j])
                    
                    return (LeftMax + RightMin) * 1.0 / 2;
                    