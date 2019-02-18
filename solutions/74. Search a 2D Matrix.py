class Solution:
    def searchMatrix(self, matrix: 'List[List[int]]', target: 'int') -> 'bool':
        if ((len(matrix) == 0) or (not matrix) or (len(matrix[0]) == 0)):
            return False;
        
        ncol = len(matrix[0])
        start = 0
        end = len(matrix) - 1
        while start + 1 < end:
            mid = (end - start)//2 + start
            if matrix[mid][0] == target:
                return True;
            elif matrix[mid][0] < target:
                start = mid
            else:
                end = mid
        if ((matrix[start][0] == target) or (matrix[end][0] == target) or (matrix[start][ncol-1] == target) or (matrix[end][ncol-1] == target)):
            return True;
        elif ((matrix[end][0] < target) & (matrix[end][ncol-1] > target)):
            T = end
        elif ((matrix[start][0] < target) & (matrix[start][ncol-1] > target)):
            T = start
        else:
            return False;
            
        start = 0
        end = ncol - 1
        while (start + 1 < end):
            mid = (end - start)//2 + start
            if matrix[T][mid] == target:
                return True;
            elif matrix[T][mid] < target:
                start = mid
            else:
                end = mid
        if ((matrix[T][start] == target) or (matrix[T][end] == target)):
            return True;
        else:
            return False;