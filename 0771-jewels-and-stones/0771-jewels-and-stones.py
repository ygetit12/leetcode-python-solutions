class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        n=0
        for char in jewels:
            for ch in stones:
                if char==ch:
                    n=n+1
        return n