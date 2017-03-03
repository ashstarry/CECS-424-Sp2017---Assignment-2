def get_primes(nb):
    while (True):
        yield nb
        nb += 2

def is_prime(nb):
    if nb == 1:
        return False
    if nb == 2:
        return True
    elif nb % 2 == 0:
        return False
    for i in range(3, int(nb ** 0.5) + 1, 2):
        if nb % i == 0:
            return False
    return True

def sum_primes():
    list = get_primes(3)
    total = 2


    for i in list:
        if (i > 2000000):
            break
        if (is_prime(i)):
            total += i

    return total

if __name__ == '__main__':
    Total = sum_primes()
    print(Total)