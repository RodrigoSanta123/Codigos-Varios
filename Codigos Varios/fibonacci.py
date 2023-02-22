def fib(n):
    a=b=1
    for i in range(n):
        yield a
        c=a+b
        a=b
        b=c
for i in fib(10):
    print(i)