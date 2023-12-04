class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for x in range(len(nums)):         
            for i in range(len(nums)):
                if i == x:
                    continue
                else:
                    result = nums[i] + nums[x]
                    if result == target:
                        return [x, i]

instance = Solution()

nums = [2,7,11,15]
target = 9

p = instance.twoSum(nums, target)
print(p)