#CPF = 461 346 879 
#SENHA = 346548

import os

x = 461
y = 346
z = 879  

c = int(input("Insira os primeiros 3 digitos do CPF aqui:"))
p = int(input("Insira os proximos 3 digitos do CPF aqui:"))
f = int(input("Insira os ultimos 3 digitos do CPF aqui:")) 

if c < x:
    print("CPF incorreto")
elif c > x:
    print("CPF incorreto")
elif p > y:
    print("CPF incorreto")
elif p < y:
    print("CPF incorreto")
elif f > z:
    print("CPF incorreto")
elif f < z:
    print("CPF incorreto")
else:
    print("CPF correto")

senha = int(input("Insira a senha aqui:"))

s = 346548

if senha < s:
    print("Senha incorreta")
elif senha > s:
    print("Senha incorreta")
else:
    print("Senha correta")

print("Verificando...")

if c == x and p == y and f == z and senha == s:
    print("CPF correto e Senha correta")
elif c == x and p == y and f == z and senha > s or senha < s:
    print("CPF correto e Senha incorreta")
elif c > x or c < x or p > y or p < y or f > z or f < z or senha == s:
    print("CPF incorreto e Senha correta")
else:
    print("CPF incorreto e Senha incorreta")

#outra forma

c = int(input("Insira os primeiros 3 digitos do CPF aqui:"))
p = int(input("Insira os proximos 3 digitos do CPF aqui:"))
f = int(input("Insira os ultimos 3 digitos do CPF aqui:"))

x = int(input("Informe a senha:"))

a = 461
b = 346
d = 879

e = 346548
if a == c and b == p and d == f:
    print("CPF valido")
    g = 1

if e == x:
    print("Senha correta")
    h = 1

if g == 1 and h == 1:
    print("Acesso autorizado")
else:
    print("CPF ou Senha invalidos")


os.system("pause")