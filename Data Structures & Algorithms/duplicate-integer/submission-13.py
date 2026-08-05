class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i not in hashset:
                hashset.add(i)
        if len(hashset) == len(nums):
            return False
        else:
            return True