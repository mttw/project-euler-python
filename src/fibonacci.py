def fibonaccis():
    a = 0
    b = 1
    yield a
    yield b
    while True:
        next = a + b
        yield next
        a = b
        b = next

def fibonacci(n):
    fibs = zip(range(0, n + 1), fibonaccis())
    return fibs[n][1]
    
        
