class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l=[]
        r=0
        s=0
        m=1
        for char in str(n):
            digit = int(char)  
            l.append(int(char))
        for i in range(len(l)):
            s=l[i]+s
            m=l[i]*m
        r=m-s
        return r