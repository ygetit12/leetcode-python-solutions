# class Solution:
#     def fizzBuzz(self, n: int) -> list[str]:
#         result = []
#         for i in range(1, n + 1):
#             if i % 15 == 0:
#                 result.append("FizzBuzz")
#             elif i % 3 == 0:
#                 result.append("Fizz")
#             elif i % 5 == 0:
#                 result.append("Buzz")
#             else:
#                 result.append(str(i))
#         return result

class Solution:
     def fizzBuzz(self, n: int) -> list[str]:
        result=[]
        for i in range(1,n+1):
            s=""
            if i%3==0:
                s+="Fizz"
            if i%5==0:
                s+="Buzz"
            result.append(s or str(i))
        return result