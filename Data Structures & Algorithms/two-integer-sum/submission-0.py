class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            current_number = nums[i]
            seen[current_number] = i
        for i in range(len(nums)):
            current_number = nums[i]
            number_needed = target - current_number
            if number_needed in seen and seen[number_needed] != i:
                return[i, seen[number_needed]]
        return[]
        