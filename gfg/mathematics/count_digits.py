def get_digit_count(num: int):
    # num_str = str(num)
    # return len(num_str)

    digit_count = 0
    # O(n)
    while num > 0:
        num = num // 10 # integer division
        digit_count += 1

    return digit_count

if __name__ == "__main__":
    num = int(input())
    num_digits = get_digit_count(num)
    print(num_digits)