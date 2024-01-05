def prime_checker(number):
    prime = 0
    for n in range(1, number+1):
        if number % n == 0:
            prime += 1
    if number == 2:
        print("It's a prime number.")
    elif prime == 2:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


prime_checker(12)

