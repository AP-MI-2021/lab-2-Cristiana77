'''
Problema:1
'''

def is_prim(n):
    if n<2:
        return False
    if n==2:
        return True
    for d in range(2,n//2+1):
        if n%d==0:
            return False
    return True

def get_largest_prime_below(n):
    '''
    Cel mai mare numar prim mai mic decat un numar dat
    :param n: nr natural
    :return: Numarul daca exista un cel mai mare numar prim mai mic decat un numar dat si False, altfel
    '''
    c=0
    if n<=2:
        return False
    for i in range(1,n):
        if is_prim(i):
            c=i
    return c
pass

def test_get_largest_prime_below():
    assert get_largest_prime_below(15) == 13
    assert get_largest_prime_below(16) == 13
    assert get_largest_prime_below(29) == 23
    assert get_largest_prime_below(33) == 31
    assert get_largest_prime_below(2) == False

test_get_largest_prime_below()

'''
Problema:5
'''

def is_palindrome(n) -> bool:
    '''
    Verificare daca este palindrom
    :param n: nr natural
    :return: True daca n este palindrom si False, altfel
    '''
    x = n
    og = 0
    while (x != 0):
        og = og * 10 + x % 10
        x = x // 10
    if (og == n):
        return True
    return False
pass

def test_is_palindrome():
     assert is_palindrome(1221) == True
     assert is_palindrome(87978) == True
     assert is_palindrome(586) == False
     assert is_palindrome(4530) == False
     assert is_palindrome(2) == True
     assert is_palindrome(74) == False

test_is_palindrome()

'''
Problema:6
'''
def is_prim(n):
    if n<2:
        return False
    if n==2:
        return True
    for d in range(2,n//2+1):
        if n%d==0:
            return False
    return True

def is_superprime(n) -> bool :
    '''
    Verificare daca este superprim
    :param n: nr natural
    :return: True daca n este superprim si False, altfel
    '''
    while (n!=0):
        if (is_prim(n) == False):
            return False
        n = n // 10
    return True
pass

def test_is_superprime():
    assert is_superprime(233) == True
    assert is_superprime(237) == False

test_is_superprime ()

def main():
    a=int(input("Problema:"))
    if (a==1):
        # is largest prime below
        n=int(input("n="))
        print(get_largest_prime_below(n))
        test_get_largest_prime_below()
    if (a==5):
        # is palindrom
        n=int(input("n="))
        print(is_palindrome(n))
        test_is_palindrome()
    if (a==6):
        # is superprime
        n=int(input("n="))
        print(is_superprime(n))
        test_is_superprime()

if __name__ == '__main__':
  main()
