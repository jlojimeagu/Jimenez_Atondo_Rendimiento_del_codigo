import datetime
def bucle (n):
   operacion = (n-1)+(n-2)
   return operacion
start_time = datetime.datetime.now()

print(bucle(40))
end_time = datetime.datetime.now()
print("El tiempo de ejecución es:", end_time - start_time)
