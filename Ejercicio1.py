import datetime
start_time = datetime.datetime.now()
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(40))

end_time = datetime.datetime.now()
print("El tiempo de ejecución es:", end_time - start_time)

