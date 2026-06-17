class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums[:-1]:
            for j in nums[nums.index(i)+1:]:
                print(i,j)
                if i + j == target:
                    if i == j:
                        result = [nums.index(i)]
                        nums.pop(nums.index(i))
                        print(nums)
                        result.append((nums.index(i)+1))
                        return result
                    result = [nums.index(i),nums.index(j)]
                    return result
                else:
                    continue
