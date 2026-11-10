class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        st=set()
        for i in range(len(nums)):
            st.add(nums[i])
        if len(st)!=len(nums):
            return True
        else:
            return False