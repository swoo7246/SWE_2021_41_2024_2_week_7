from typing import List
def twoSum(nums: List[int], target:int) -> List[int]:
    length = len(nums)
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] + nums[j] == target:
                return [i, j]
    