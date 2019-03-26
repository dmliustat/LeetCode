class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # The first step is to remove duplicates. Since there is no 
        # duplicates, we can skip that.
        
        # Then sort candidates
        candidates.sort()
        
        results = []
        # if candidates == None or len(candidates) == 0:
        #     return results;
        
        self.helper(candidates, target, 0, [], results)
        
        return results;
    
    # 1. Define recursion. 
    # The argument index denotes the starting index. The chosen
    # numbers are stored in combination
    def helper(self, candidates, target, index, combination, results):
        # 3. Exit
        if (target == 0):
            results.append(list(combination))
            return;
        
        # 2. Dismantle recursion
        for i in range(index, len(candidates)):
            if candidates[i] > target:
                break;
            
            combination.append(candidates[i])
            self.helper(candidates, target - candidates[i], i, combination, results)
            combination.pop() # backtracking
            

