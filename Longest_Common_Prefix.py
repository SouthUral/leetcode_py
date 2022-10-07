

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        substring = []
        for counter, simb in enumerate(sorted(strs, key=len)[0]):
            if all(map(lambda x: simb if x[counter] == simb else False, strs)):
                substring.append(simb)
            else:
                break
        return ''.join(substring)
            

t1 = ["flower","flow","flight"], 'fl'
t2 = ["dog","racecar","car"], ''
t3 = ['getrs', 'getter', 'gertrude'], 'ge'
t4 = ['subject', 'subjective', 'substruct'], 'sub'
t5 = ['boston', 'buy', 'bruclin'], 'b'
t6 = ['', '', ''], ''
t7 = ['a'], 'a'
t8 = ['ab', 'a'], 'a'

def test_func(*args):
    obj = Solution()
    for set in args:
        array = set[0]
        answer = set[1]
        res = obj.longestCommonPrefix(array)
        assert res == answer, f'test faild, expected value: "{answer}", the resulting value: "{res}"'
        print(f'the test case: "{set}" is passed')
    print('all tests are completed')

test_func(t1, t2, t3, t4, t5, t6, t7, t8)
