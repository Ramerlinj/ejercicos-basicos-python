l = int(input())
# "AIDOOXODIXD"
s = input().strip() 
ipu = list(map(int,input().split()))

def busqueda(busqueda,s):
    p=[]
    for i in range(len(s)):
        if s[i] == busqueda:
            p.append(i)
    return p

lista_O=busqueda('O',s)
lista_D=busqueda('D',s)
lista_I=busqueda('I',s)

n= ipu[0]
m= ipu[1]
k= ipu[2]

if len(lista_O) < n or len(lista_D) < m or len(lista_I) < k:
    print("-1")

max_largo = -1

for i in range(l):
    for j in range(i, l):
        subcadena = s[i : j+1]
        
        c_O = subcadena.count('O')
        c_D = subcadena.count('D')
        c_I = subcadena.count('I')
        
        if c_O == n and c_D == m and c_I == k:
            largo_actual = len(subcadena)
            if largo_actual > max_largo:
                max_largo = largo_actual

print(max_largo)







