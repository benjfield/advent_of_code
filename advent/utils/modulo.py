import math

def gcd_extended(a, b):
    global x, y
 
    # Base Case
    if (a == 0):
        x = 0
        y = 1
        return b
 
    # To store results of recursive call
    gcd = gcd_extended(b % a, a)
    x1 = x
    y1 = y
 
    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1
 
    return gcd
 
def modulo_inverse(A, M):
    g = gcd_extended(A, M)
    if (g != 1):
        print("Inverse doesn't exist")
    else:
        # m is added to handle negative x
        res = (x % M + M) % M
        return res
    
def chinese_remainder_theorem(divisors_to_remainders):
    divisor_sum_product = math.prod(divisors_to_remainders.keys())

    result = 0
    for divisor, remainder in divisors_to_remainders.items():
        product_over_divisor = divisor_sum_product // divisor
        result += remainder * (product_over_divisor) * modulo_inverse(product_over_divisor, divisor)

    return result % divisor_sum_product