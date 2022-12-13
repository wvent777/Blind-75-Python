class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Using a Hash Map
    d = {} 
    for i, num in enumerate(nums):
      if target - num in d:
        return d[target - num], i 
      d[num] = i 
    
