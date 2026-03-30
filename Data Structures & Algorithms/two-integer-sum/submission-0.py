class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i,num in enumerate(nums):
            patner = target - num
            if patner in hash_map:
                return [hash_map[patner],i]
            hash_map[num] = i