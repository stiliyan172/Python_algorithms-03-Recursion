# def calc_fib(num):
#     if num <= 1:
#         return 1
#     return calc_fib(num - 1) + calc_fib(num - 2)
#
#
# print(calc_fib(int(input())))


def iterative_fib(number):
    fib_0 = 1
    fib_1 = 1
    result = 0
    for _ in range(number - 1):
        result = fib_0 + fib_1
        fib_0, fib_1 = fib_1, result

    return result


print(iterative_fib(int(input())))