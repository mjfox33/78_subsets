
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result_size = pow(2,n)
        result = []
        for i in range(result_size):
            current_set = []
            for j in range(n):
                if (i & (1<<j)) > 0:
                    current_set.append(nums[j])
            result.append(current_set)
        return result