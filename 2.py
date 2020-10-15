def is_prime(n=int(input('Enter number to check if it is prime: '))):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return 'is not prime'
        else:
            return 'is prime'


prime = is_prime()
print(prime)