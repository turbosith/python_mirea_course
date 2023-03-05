from math import ceil, floor


def main(y, x, z):
    sum1 = 0
    n = len(x)
    print(n)
    for i in range(1, n + 1):
        sum1 += ((abs(45 * (z[floor(i / 2)] ** 2) + 32 *
                      y[n - i] + (x[n - i]) ** 3)) ** 6) / 37
    return sum1


print('%.2e' %  main([0.52, -0.52, -0.74],
[-0.5, -0.56, -0.81],
[-0.27, -0.7, 0.66]))
