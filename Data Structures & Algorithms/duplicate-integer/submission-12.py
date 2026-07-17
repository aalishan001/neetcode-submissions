class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            seen.add(i)
        if len(seen) == len(nums):
            return False
        else:
            return True