class Solution(object):
    def singleNumber(self, nums):
        ans=0
        for i in range(0,32):
            count = 0
            for j in range(len(nums)):
                if (nums[j]>>i)&1:
                    count+=1
            if count%2==1:
                ans+=(2**i)
        return ans
