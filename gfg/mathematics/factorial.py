def get_factorial(n):
    # Iterative Solution
    # Theta (n)
    fact = 1
    for i in range(1, n+1):
        fact = fact*i
    
    return fact

def get_factorial_recursion(n):
    # Theta (N)
    # Auxilary Space : Theta (N)
    if n == 0:
        return 1
    else:
        return n*get_factorial_recursion(n-1)

if __name__ == "__main__":
    n = int(input())
    factorial = get_factorial_recursion(n)
    print(factorial)
