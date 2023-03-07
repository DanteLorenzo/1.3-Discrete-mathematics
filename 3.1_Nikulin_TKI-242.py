import math

N = 21

def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            c = a + b
            a, b = b, c
        return c
    
def fibonacci_formula(n):
    phi = (1 + math.sqrt(5)) / 2
    return int((phi ** n - (-phi) ** (-n)) / math.sqrt(5))
    

if __name__ == "__main__":
    print('№         Итерационная ф-ла             Формула для n-го числа')
    for i in range(N+1):
        print("{:<10}{:<30}{:<}".format(i,fibonacci_iterative(i),fibonacci_formula(i)))
        