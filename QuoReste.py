


a = 0
b = 0
q = 0
r = 0

print('Donner 2 entiers A et B')

print('A : ')
a = int(input())
print('B : ')
b = int(input())

q = 0
r = a

while r > b:
    q = q + 1
    r = r - b

print('Le quotient de de A/B est : '+str(q)+' Le reste de A/B : '+str(r))
