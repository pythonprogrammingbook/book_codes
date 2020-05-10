no_primes = [
    4, 6, 6, 8, 8, 9, 10, 10, 12, 12, 12, 12, 14, 14, 15, 15, 16, 16, 16
]
# 用集合自动去重
no_primes_without_duplication = list(set(no_primes))

print(no_primes_without_duplication)