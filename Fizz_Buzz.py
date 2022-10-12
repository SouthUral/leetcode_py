

from curses.ascii import SO


class Solution:
    def fizzBuzz(self, n):
        res_arr = []
        for i in range(1, n + 1):
            if i % 3 == i % 5 == 0:
                res_arr.append('FizzBuzz')
            elif i % 3 == 0:
                res_arr.append('Fizz')
            elif i % 5 == 0:
                res_arr.append('Buzz')
            else:
                res_arr.append(str(i))
        return res_arr
            

t1 = 15
obj = Solution()
print(obj.fizzBuzz(15))