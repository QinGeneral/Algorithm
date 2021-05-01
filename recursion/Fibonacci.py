map = {}


def fibonacci(n):
    if n in map:
        return map[n]
    
    val = 1
    if n == 1 or n == 2:
        return val

    val = fibonacci(n - 1) + fibonacci(n - 2)
    map[n] = val
    return val


for i in range(1, 16):
    print(fibonacci(i))
