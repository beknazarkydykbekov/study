class Solution:
    def twoSum(self, nums = [2,7,11,15], target = 9):
        for i in nums:
            for j in nums:
                if i+j == target:
                    return [nums[0], nums[1]]
        
a = Solution()
print(a.twoSum())

# class Solution:
#     def twoSum(self, nums = [2,7,11,15], target = 9):
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] == target - nums[i]:
#                     return [i, j]

# a = Solution()
# print(a.twoSum())