class Solution:
    def defangIPaddr(self, address: str) -> str:
        s=[]
        for char in address:
            if char=='.':
                s.append('[.]')
            else:
                s.append(char)
        return "".join(s)