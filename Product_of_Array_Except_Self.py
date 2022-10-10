class Solution:
    def productExceptSelf(self, nums):
        flow1 = [1]
        flow2 = [1]
        reverce_nums = nums[::-1]
        for i in range(1, len(nums)):
            flow1.append(flow1[-1] * nums[i-1])
            flow2.append(flow2[-1] * reverce_nums[i-1])
        flow2.reverse()
        return [x * y for x, y in zip(flow1, flow2)]


obj = Solution()
print(obj.productExceptSelf([1, 2, 3, 4]))

        