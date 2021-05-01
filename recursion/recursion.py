import time


# 斐波那契求和递归版本
def recursion_fabonacci_sequence(x):
    if (x == 1 or x == 2):
        return 1

    return recursion_fabonacci_sequence(x - 1) + recursion_fabonacci_sequence(x - 2)


# 斐波那契求和循环版本
def loop_fabonacci_sequence(x):
    if (x == 1 or x == 2):
        return 1

    first = 1
    second = 1
    cur = 0
    for i in range(3, x + 1):
        cur = first + second
        first = second
        second = cur
    return cur


# 最大公约数递归版本
# x >= y, x >= 1, y >= 1
def recursion_greatest_divisor(x, y):
    left = x % y
    if left == 0:
        return y

    return recursion_greatest_divisor(y, left)


# 最大公约数循环版本
# x >= y, x >= 1, y >= 1
def loop_greatest_divisor(x, y):
    left = 1
    while(True):
        left = x % y
        if (left == 0):
            return y
        x = y
        y = left


# 求和递归版本
def recursion_sum(arr):
    if len(arr) == 0:
        return 0

    if len(arr) == 1:
        return arr[0]

    last = arr.pop()
    return last + recursion_sum(arr)


# 求和循环版本
def loop_sum(arr):
    sum = 0
    for i in range(0, len(arr)):
        sum = sum + arr[i]
    return sum


def main():
    # test fabonacci sequence
    print("test fabonacci sequence")
    print(recursion_fabonacci_sequence(15))
    print(loop_fabonacci_sequence(15))

    print("***************")
    start_time = time.time()
    print(recursion_fabonacci_sequence(25))
    print(time.time() - start_time)

    print("***************")
    start_time = time.time()
    loop_fabonacci_sequence(10000)
    print(loop_fabonacci_sequence(25))
    print(time.time() - start_time)

    # test greatest common divisor
    print(recursion_greatest_divisor(188, 144))
    print(recursion_greatest_divisor(5, 4))
    print(recursion_greatest_divisor(1680, 640))

    print(loop_greatest_divisor(188, 144))
    print(loop_greatest_divisor(5, 4))
    print(loop_greatest_divisor(1680, 640))

    # test sum of array
    print(recursion_sum([1, 2, 3, 4]))
    print(loop_sum([1, 2, 3, 4]))


main()
