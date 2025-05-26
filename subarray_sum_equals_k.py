class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        '''
        TC: O(n)
        AS: O(n)
        '''
        # rSum_tracker = {rSum: Count}       
        rSum_tracker = {0:1}
        maxCount = 0
        rSum = 0

        for i in nums:
            rSum += i

            # Check 'rsum-k' before adding the rSum
            output = rSum - k 
            # if output in rSum_tracker:
            #     maxCount += rSum_tracker[output]
            maxCount += rSum_tracker.get(output, 0)

            # if rSum not in rSum_tracker:
            #     rSum_tracker[rSum] = 1
            # else:
            #     rSum_tracker[rSum] += 1
            rSum_tracker[rSum] = rSum_tracker.get(rSum, 0) + 1

        return maxCount
    
nums = [1]
k = 0

x = Solution()
print(x.subarraySum(nums, k))