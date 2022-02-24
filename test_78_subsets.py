from code_78_subsets import Solution

def test_example_1():
    s = Solution()
    nums = [1,2,3]
    output = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    assert s.subsets(nums) == output