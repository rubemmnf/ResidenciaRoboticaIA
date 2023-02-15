import time

# t = time.time()
# print(t)

# localtime = time.localtime()
# ano, mes, dia = localtime[0], localtime[1], localtime[2]
# print(str(dia)+"/"+str(mes)+"/"+str(ano))

# t_0 = time.time()
t_0 = time.perf_counter()
x = 0
while x < 100000000:
    x+=1
t_final = time.perf_counter()

diferenca = t_final - t_0
print(diferenca)