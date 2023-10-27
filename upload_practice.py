def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_mersenne_primes(limit):
    for n in range(2, limit):
        mersenne_candidate = 2 ** n - 1
        if is_prime(mersenne_candidate):
            print(f"Mersenne prime for n={n} is {mersenne_candidate}")

# 30までのnについてメルセンヌ素数を探す
find_mersenne_primes(30)
