class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        l=[]
        su=0
        for i  in range(len(nums)):
            su=nums[i]+su
            l.append(su)
        return l