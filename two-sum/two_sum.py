class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmp = {}
        for i in range(len(nums)):
            hmp[nums[i]] = i
        
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hmp and hmp[comp] != i:
                return [i, hmp[comp]]

