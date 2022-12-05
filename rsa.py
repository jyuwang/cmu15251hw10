import typing

encryptedMessage = 163077576587089932277514178989798339755826189700674110151160860819557757512053108465634676999401755817425637794522932574265893488854028596522889419543378155476439015236106447427921542963150735762104095795184542


def totient(P, Q):
    return (P-1) * (Q-1)


def modularInverse(integer, modulo):
    # what is a modular inverse
    # A * A^-1 .   mod x = 1
    # A^-1 is an element of Zn
    # Zn is a set of all numbers from 1 to n-1
    # in this case n is psi(n), which just happens to be the modulo argument
    for i in range(2, modulo):
        if (integer * i) % modulo == 1:
            return i


def modularInverseV2(integer, modulo):

    def gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            y, x = gcd(b % a, a)
            return (x-(b//a)*y, y)

    x, y = gcd(integer, modulo)
    return x % modulo


def FME(base, exponent, modulo):
    result = 1
    while exponent > 1:
        if exponent & 1:
            result = (result * base) % modulo
        base = (base * base) % modulo
        exponent >>= 1
    return (base * result) % modulo


def numToString(num):
    alphabet = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = ''
    while num > 0:
        index = num % 27
        num = num // 27
        result = alphabet[index] + result
    return result


def decrypt(p: int, q: int, e: int, c: int) -> str:
    n = p*q

    psi = totient(p, q)
    inverseE = modularInverseV2(e, psi)
    m = FME(c, inverseE, n)

    return numToString(m)


# print("The original message was: ", decrypt(7, 11, 13, 5))
