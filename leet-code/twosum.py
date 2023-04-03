from typing import List


class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     indices = []
    #     for i in range(len(nums) - 1):
    #         if nums[i] + nums[i+1] == target:
    #             indices += [i, i+1]
    #
    #     return indices

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}
        for index, val in enumerate(nums):

            rem = target - val
            if rem in d:
                return [index, d[rem]]
            d[val] = index


solution = Solution()
print(solution.twoSum([2,7,11,15], 9))

