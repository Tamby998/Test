a = 0
b = 0
p = 0
i = 0

print('Entrer 2 entiers A et B :')
print('A : ')
a = int(input())
print('B : ')
b = int(input())

if a == 0 and b == 0:
    p = 0
else:
    p = 0
    for i in range(b):
        p = p+a

print('Le produit A*B : '+ str(p))
