def isPalindrome(x):
    x_str = str(x)
    x_len = len(x_str)
    if x < 0:
        return False
    elif x_len % 2 == 0:
        a = x_str[:x_len//2]
        b = x_str[x_len//2:][::-1]
        return a == b
    else:
        a = x_str[:x_len//2 + 1]
        b = x_str[x_len//2::][::-1]
        return a == b
print(isPalindrome(11))