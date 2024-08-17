def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
        
#yield makes the fibonacci(n) function a generator.

def cube(x):
    #Cubes 
    return x ** 3


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


