class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i,j in enumerate(nums):
            if target-j in dict:
                return sorted([i,dict[target-j]])
            dict[j]=i
