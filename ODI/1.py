l = int(input())
s = input().strip() 
ipu = list(map(int, input().split()))

n = ipu[0]
m = ipu[1]
k = ipu[2]

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