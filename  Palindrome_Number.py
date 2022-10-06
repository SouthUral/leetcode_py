def isPalindrome(x):
    x_str = str(x)
    x_len = len(x_str)
    if x_len % 2 == 0:
        return x_str[:x_len//2] == x_str[x_len//2:][::-1]
    else:
        return x_str[:x_len//2 + 1] == x_str[x_len//2::][::-1]
print(isPalindrome(11))


def isPalindrome_2(x):
    str_number = str(x)
    rev_number = str_number[::-1]
    return str_number == rev_number

print(isPalindrome_2(121))