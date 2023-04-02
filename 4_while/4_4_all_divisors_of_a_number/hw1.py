# Дано натуральное число N. Определить, является ли оно простым.
# Натуральное число N называется простым, если у него есть только два делителя:
# единица и само число N.

# В качестве ответа выведите "Yes", если число простое,  "No" - в противном случае.

# Sample Input:

# 5
# Sample Output:

# Yes

# import collections
# import itertools
#
#
# def get_prime_divisors(n):
#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#             n /= i
#             yield i
#         else:
#             i += 1
#
#     if n > 1:
#         yield n
#
#
# def calc_product(iterable):
#     acc = 1
#     for i in iterable:
#         acc *= i
#     return acc
#
#
# def get_all_divisors(n):
#     primes = get_prime_divisors(n)
#
#     primes_counted = collections.Counter(primes)
#
#     divisors_exponentiated = [
#         [div ** i for i in range(count + 1)]
#         for div, count in primes_counted.items()
#     ]
#
#     for prime_exp_combination in itertools.product(*divisors_exponentiated):
#         yield calc_product(prime_exp_combination)
#
#
# print('Yes' if len(list(get_all_divisors(int(input())))) == 2 else 'No')


n=int(input())
d = 2
while n!=1 and n % d != 0:
    d += 1
print("Yes" if n==d else "No")
