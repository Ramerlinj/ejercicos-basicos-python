# # n = int(input()) #intentos
r = list(map(int,input().split()))

re = []
for i in r:
    raiz = i ** 0.5
    resultado = raiz * raiz
    print(resultado == i)
    if isinstance(resultado, int) or (isinstance(resultado, float) and resultado.is_integer()):
        re.append(i)
    else:
        print('decimal')

print(re)
# tr = 10404
# tra = tr**0.5
# print(tra)
# print(tra * tra == tr )





#!me quede porque no se literalmente como voy a sacar la raiz, osea basicamente
#!como saber si un numeor es raiz perfecta