class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if((not matrix) or (len(matrix) == 0) or (len(matrix[0]) == 0)):
            return False;
        
        ncol = len(matrix[0])
        for i in range(len(matrix)):
            if ((matrix[i][0] == target) or (matrix[i][ncol-1] == target)):
                return True;
            elif ((matrix[i][0] < target) and (matrix[i][ncol-1] > target)):
                start = 0
                end = ncol-1
                while start + 1 < end:
                    mid = (end - start)//2 + start
                    if (matrix[i][mid] == target):
                        return True;
                    elif (matrix[i][mid] < target):
                        start = mid
                    else:
                        end = mid
                if((matrix[i][start] == target) or (matrix[i][end] == target)):
                    return True;
        
            elif (matrix[i][0] > target):
                return False;
            
        return False;