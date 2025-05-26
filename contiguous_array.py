class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        '''
        TC: O(n)
        AS: O(n)
        '''
        # rSum_tracker = {rsum: index}
        rSum_tracker = {0:-1}
        maxSum = 0
        rSum = 0

        for idx, element in enumerate(nums): #always use enumerate for indexing
            if element == 0:
                rSum -= 1
            else:
                rSum += 1

            if rSum not in rSum_tracker:
                rSum_tracker[rSum] = idx
            else:
                maxSum = max(maxSum, idx  - rSum_tracker[rSum])

        return maxSum

nums = [0,1,1,1,1,1,0,0,0]
x = Solution()
print(x.findMaxLength(nums))