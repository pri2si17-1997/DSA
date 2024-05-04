def get_factorial(n):
    # Iterative Solution
    # Theta (n)
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    
    return fact

def get_trailing_zero_count(n):
    # Theta (N) time comlexity
    # Theta (1) space complexity

    # This method will get into overflow as for 
    # n >= 20, factorial will be very large
    count = 0
    factorial = get_factorial(n)
    while factorial % 10 == 0:
        count += 1
        factorial /= 10
    
    return count

def get_trailing_zero_count_log_n(n):
    # This uses special property 
    # that factorial will have 0 only if its
    # multiple of 5

    # zero_count = floor(n/5) + floor(n/25) + floor(n/125)

    # Time complexity: theta(log n)
    # space complexity: theta (1)

    i = 5
    zero_count = 0
    while i<=n:
        zero_count += n // i
        i *= 5
    
    return zero_count


if __name__ == "__main__":
    n = int(input())
    trailing_zeros = get_trailing_zero_count_log_n(n)
    print(trailing_zeros)