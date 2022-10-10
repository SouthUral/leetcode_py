from curses.ascii import SO
from functools import reduce


class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or len(s) <= numRows:
            return s
        interval = numRows - 2 
        first_matrix = []
        while s != []:
            row = list(s[:numRows])
            if len(row) < numRows:
                row.extend(['']*(numRows-len(row)))
            first_matrix.append(row)
            s = list(s[numRows:])
            for i in range(interval):
                if s != []:
                    interval_row = [""]*numRows
                    interval_row[i+1] = s.pop(0)
                    first_matrix.append(interval_row[::-1])
        nz = list(map(list, zip(*first_matrix)))
        return ''.join(reduce(lambda x, y: x + y , nz))
        
        




t1 = ('PAYPALISHIRING', 3), "PAHNAPLSIIGYIR", 1
t2 = ('PAYPALISHIRING', 4), "PINALSIGYAHRPI", 2
t3 = ("ABCDE", 4), "ABCED", 3
t4 = ('A', 2), "A", 4
t5 = ('ABC', 2), "ACB", 5
t6 = ('ABCD', 2), 'ACBD', 6

def test(*args):
    obj = Solution()
    for arg in args:
        string, row = arg[0]
        try_answer = arg[1]
        number_test = arg[2]
        answer = obj.convert(string, row)
        assert answer == try_answer, f'test "{number_test}" was fail, get item: "{answer}"'
        print(f'test "{number_test}" sucsess')


cases_test = [t1, t2, t3, t4, t5, t6]
test(*cases_test)

