import matplotlib.pyplot as plt


# Вычисляем первые 20 чисел Фибоначчи
fibonacci = [0, 1]
for i in range(18):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

# Вычисляем отношения двух последовательных чисел Фибоначчи
ratios = []
for i in range(len(fibonacci) - 1):
    if fibonacci[i] != 0:
        ratio = fibonacci[i+1] / fibonacci[i]
        ratios.append(ratio)


def matplot():
    plt.scatter(range(len(ratios)),ratios, s = 20, c = 'green')
    plt.grid(True)
    
    # Настраиваем оси и заголовок
    plt.ylim([0, 3])
    plt.xlabel('Номер числа Фибоначчи')
    plt.ylabel('Отношение двух последовательных чисел Фибоначчи')
    plt.title('Отношения двух последовательных чисел Фибоначчи')

    plt.show()

if __name__ == "__main__":
    matplot()
