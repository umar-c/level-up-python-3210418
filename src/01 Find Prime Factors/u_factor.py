def get_prime_factors(number):
  
  prime_factors = []
  divisor = 2
  while divisor <= number:
    if number % divisor == 0:
      prime_factors.append(divisor)
      number = number//divisor
    else:
      divisor += 1

  return prime_factors
      
if __name__ == '__main__':
    print(get_prime_factors(-1))
    print(get_prime_factors(0))
    print(get_prime_factors(1))
    print(get_prime_factors(2))
    print(get_prime_factors(13))    # [13]
    print(get_prime_factors(630))   # [2, 3, 3, 5, 7]
    print(get_prime_factors(739348943454354394357))