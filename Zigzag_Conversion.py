from curses.ascii import SO
from functools import reduce


class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        interval = numRows - 2
        first_matrix = []
        while s != []:
            row = list(s[:numRows])
            if len(row) < numRows:
                row.extend(['' for _ in range(numRows-len(row))])
            first_matrix.append(row)
            second = list(s[numRows:])
            if second != []:
                for i in range(interval):
                    interval_row = ["" for _ in range(numRows)]
                    interval_row[i+1] = second.pop(0)
                    first_matrix.append(interval_row[::-1])
                    if second == []:
                        break
                s = second
            else:
                break
        print(first_matrix)
        nz = list(map(list, zip(*first_matrix)))
        print(nz)
        return ''.join(reduce(lambda x, y: x + y , nz))
        
        




t1 = ('PAYPALISHIRING', 3), "PAHNAPLSIIGYIR", 1
t2 = ('PAYPALISHIRING', 4), "PINALSIGYAHRPI", 2
t3 = ("ABCDE", 4), "ABCED", 3

def test(*args):
    obj = Solution()
    for arg in args:
        string, row = arg[0]
        try_answer = arg[1]
        number_test = arg[2]
        answer = obj.convert(string, row)
        assert answer == try_answer, f'test "{number_test}" was fail, get item: "{answer}"'
        print(f'test "{number_test}" sucsess')

test(t1, t2, t3)

