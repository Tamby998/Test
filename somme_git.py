'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
i = 0
n = 0
s = 0

print('Donner un entier N : ')
n = int(input())

for i in range(n):
    s+=i+1
    
print('sommme : '+str(s))