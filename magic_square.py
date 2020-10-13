from random import randint

d = int(input("d = "))
Va = []

def tab(a):
    x = []
    s = []
    n = 0
    z = 0
    
    while z < a:
        s = []
        n = 0
        while n < a:
            v = randint(0, 10)
            s.append(v)
            n = n + 1
        x.append(s)
        z = z + 1
        
    return(x)

tab = tab(d)
print("tab ", tab)
print("")

def somme_ligne(tab):
    V = []
    i = 0
    u = 0
    while i < len(tab):
        z = tab[i]
        x = sum(z)
        V.append(x)
        i = i + 1
    return(V)

Va.append(somme_ligne(tab))

def somme_colone(tab):
    i = 0
    u = 0
    w = []
    while u < len(tab):
        n = 0
        x = 0
        
        while n < len(tab):
            z = tab[n]
            s = z[u]
            x = x + s
            n = n + 1
        w.append(x)
        
        u = u + 1
    return(w)

Va.append(somme_colone(tab))


def somme_diagonal(tab):
    x = 0
    w = 0
    n = 0
    u = len(tab)
    g = u - 1
    y = []
    
    V = []
    
    while n < u:
        z = tab[n]
        w = g - n
        s = z[w]
        y.append(s)
        n = n + 1
    V.append(sum(y))
    
    x = 0
    w = 0
    n = 0
    u = len(tab)
    g = u - 1
    y = []
    
    while n < u:
        z = tab[n]
        s = z[n]
        y.append(s)
        n = n + 1
    V.append(sum(y))
    
    return(V)

Va.append(somme_diagonal(tab))

print("")
print("validation ", Va)

S = []

def liste(x):
    z = []
    n = 0
    
    while n < len(x):
        if type(x[n]) != list:
            S.append(x[n])
            
        if type(x[n]) == list:
            z = x[n]
            liste(z)
        n = n + 1
            
    return(S)

Valid = sorted(liste(Va))

print(Valid)

f = len(Valid) - 1

print(Valid[0])

print(Valid[f])

if Valid[0] == Valid[f]:
    print("ce carré est magique")
else:
    print("ce carré n est pas magique")
