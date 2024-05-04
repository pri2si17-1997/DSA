def is_palindrome(num: int)->bool:
    # pythonic way
    # num_str = str(num)
    # reverse_str = num_str[::-1]

    # return num_str == reverse_str

    # num_str = str(num)
    # i = 0
    # j = len(num_str) - 1
    # while i < j:
    #     if num_str[i] != num_str[j]:
    #         return False
    #     i += 1
    #     j -= 1
    
    # return True

    reverse_num = 0
    original_num = num

    while num > 0:
        digit = num % 10
        reverse_num = reverse_num*10 + digit
        num = num // 10

    return reverse_num == original_num

if __name__ == "__main__":
    num = int(input())
    print(is_palindrome(num=num))