import math
def is_prime(n):
    """
   判断一个数是否为素数
   ----------------------
   返回值： True,是素数
           False,不是素数
    """
    return n > 1 and all(n % i for i in range(2, int(math.sqrt(n)) + 1))
    
twin_primes = {(x, x + 2)
               for x in range(1, 100, 2) if is_prime(x) and is_prime(x + 2)}

print(twin_primes)