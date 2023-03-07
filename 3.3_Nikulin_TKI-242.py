import matplotlib.pyplot as plt
import math

N = 18

# Вычисляем первые 20 чисел Фибоначчи
fibonacci = [0, 1]
for i in range(N):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

# Вычисляем отношения двух последовательных чисел Фибоначчи
ratios = []
for i in range(len(fibonacci) - 1):
    if fibonacci[i] != 0:
        ratio = fibonacci[i+1] / fibonacci[i]
        ratios.append(ratio)

# Вычисляем отклонения отношений от золотого сечения
golden_ratio = (1 + math.sqrt(5)) / 2
deviations = []
for ratio in ratios:
    deviation = ratio - golden_ratio
    deviations.append(deviation)


def matplot():
    plt.figure(figsize=(10,7))
    plt.scatter(range(len(deviations)), deviations, s = 20, c = 'green')
    plt.grid(True)

    plt.ylim([-0.7, 0.7])
    plt.xlabel('Номер числа Фибоначчи')
    plt.ylabel('Отклонение от золотого сечения')
    plt.title('Отклонения отношений двух последовательных чисел Фибоначчи от золотого сечения')

    plt.show()

if __name__ == "__main__":
    matplot()
    print('№         Отклонения отношений от золотого сечения             Отклонения отношений от золотого сечения')
    for i in range(N):
        print("{:<10}{:<53}{:}".format(i+1, ratios[i], deviations[i]))


