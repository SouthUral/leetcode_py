from functools import reduce

class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     substrings = [(s, False)]
    #     while s != '':
    #         sub, s = self.find_first_substring(s)
    #         substrings.append(sub)
    #     return self.check_longest_sub(substrings)

    # def find_first_substring(self, s: str) -> str:
    #     substring = []
    #     for counter, i in enumerate(s, start=1):
    #         if i not in substring:
    #             substring.append(i)
    #         else:
    #             substring.append(i)
    #             return (''.join(substring), False), s[1:]
    #     return (''.join(substring), True), ''

    # def check_longest_sub(self, substrings):
    #     max_sub = ''
    #     for items in substrings:
    #         if items[0] == items[0][::-1] and items[1] is False:
    #             max_sub = items[0] if len(items[0]) > len(max_sub) else max_sub
    #         else:
    #             max_sub = items[0][0] if len(items[0][0]) > len(max_sub) else max_sub
    #     return max_sub

    def longestPalindrome(self, s):
        substrings = set()
        for counter, i in enumerate(s, start=1):
            second_s = s[counter:]
            sub_s = s[counter-1:]
            if i in second_s:
                indexes = self.find_indexes(i, sub_s)
                substrings.update(self.slicing(indexes, sub_s))
            else:
                substrings.add(i)
        sub_palindrome = [i for i in substrings if self.isPalindrome(i)]
        return reduce(lambda x, y: x if len(x)>= len(y) else y ,sub_palindrome)

    def slicing(self, index_box, sub_s):
        res_box = set()
        for i in index_box:
            res_box.add(sub_s[:i+1]) # возможна ошибка
        return res_box

    def find_indexes(self, item, items):
        indexes_item = []
        for counter, i in enumerate(items):
            if i == item:
                indexes_item.append(counter)
        return indexes_item

    def isPalindrome(self, x):
        str_number = str(x)
        rev_number = str_number[::-1]
        return str_number == rev_number

obj = Solution()
t1 = "babad"
t2 = "cbbd"
t3 = 'ac'
t4 = 'accc'
t5 = 'nccaccab'
print(obj.longestPalindrome(t1))
print(obj.longestPalindrome(t2))
print(obj.longestPalindrome(t3))
print(obj.longestPalindrome(t4))
print(obj.longestPalindrome(t5))
