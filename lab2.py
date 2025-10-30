#вариант 3

#Средней сложности:
#3. Факториал числа.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#5. Список простых чисел до 100.
def prime_number(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
            else:
                return True
