a = int(input())
fib = [0,1]
for i in range(a-1):
    res = fib[-1] + fib[-2]
    fib.append(res)
    
print(*fib)

a = int(input())
def fib(n):
    a, b = 0, 1
    for i in range(n+1):
        yield a
        a, b = b, a + b
print(*list(fib(a)))

