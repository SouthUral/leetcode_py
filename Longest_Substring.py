

class Solution:
    def lengthOfLongestSubstring(self, s):
        substrings_lens = [0]
        while s != '':
            len_sub, s = self.find_substring(s)
            substrings_lens.append(len_sub)
        return max(substrings_lens)
  
    def find_substring(self, string):
        substring = []
        for item in string:
            if item not in substring:
                substring.append(item)
            else:
                break
        len_max = len(substring)
        second_items = string[string.index(item)+1:]
        return len_max, second_items


obj_sol = Solution()    


def test_func(test_item, true_answer):
    res_test = obj_sol.lengthOfLongestSubstring(test_item)
    assert res_test == true_answer, f'значение не верное: {res_test} с входящим значением "{test_item}", ожидаемое значение "{true_answer}"'


t_1 = ("pwwkew", 3)
t_2 = ("abcabcbb", 3)
t_3 = (' ', 1)
t_4 = ('', 0)
t_5 = ('au', 2)
t_6 = ('aab', 2)
t_7 = ('dvdf', 3)
t_8 = ('anviaj', 5)

test_func(*t_1)
print('test_1: successful')
test_func(*t_2)
print('test_2: successful')
test_func(*t_3)
print('test_3: successful')
test_func(*t_4)
print('test_4: successful')
test_func(*t_5)
print('test_5: successful')
test_func(*t_6)
print('test_6: successful')
test_func(*t_7)
print('test_7: successful')
test_func(*t_8)
print('test_8: successful')
