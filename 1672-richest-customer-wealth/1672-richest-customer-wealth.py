class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
      t=0
      for i in accounts:
        s=sum(i)
        if s>t:
            t=s
      return t