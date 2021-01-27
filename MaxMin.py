'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

i = 0
n = 0
Max = 0
Min = 0
x = 0

tab = []

print('Entrez un nombre > 0')
n = int(input())

if n > 0:
    for i in range(n):
        print('Entrer le chiffre num-'+str(i+1))
        tab.append(int(input()))
    
    Min = tab[0]
    Max = tab[0]
    
    for i in range(n):
        if tab[i] < Min:
            Min = tab[i]
        
        if tab[i] > Max:
            Max = tab[i]
    
    print('Max = '+str(Max)+' Min = '+str(Min))
            
else:
    print('Nombre inférieur ou sup à zero')
