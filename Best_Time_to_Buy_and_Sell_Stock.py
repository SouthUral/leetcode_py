class Solution:
    def maxProfit(self, prices):
        max_profit = -float('inf')
        min_price = float('inf')
        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p - min_price)
        return max_profit


 






t1 = [7,1,5,3,6,4], 5, 1

def test(*args):
    obj = Solution()
    for arg in args:
        inp_array = arg[0]
        try_answer = arg[1]
        number_test = arg[2]
        answer = obj.maxProfit(inp_array)
        assert answer == try_answer, f'test "{number_test}" was fail, get item: "{answer}"'
        print(f'test "{number_test}" sucsess')

test(t1)