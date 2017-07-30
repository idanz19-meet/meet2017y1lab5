#Fibonacci

def fib(n):
    fi = 1
    se = 1
    for i in range(n):
        store = fi
        fi = se
        se = store + fi
    return(store)

#Factorial

def fact(n):
    num = 1
    for i in range(n):
        num = num*(i + 1)
    return(num)
