a = 0
b = 0
r = 0

print('Donner 2 entiers positif A et B')

print('A : ')
a = int(input())
print('B : ')
b = int(input())

r = a

while  r > 0:
    r = r - b
    
if r == 0:
    print('A est Divisible par B')
else:
    print('A n\'est pas divisible par B')
