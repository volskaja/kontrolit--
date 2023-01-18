from math import * 
from random import *

#4 variant
#1
pin = ['  ^---^   ',
       ' ( o o )  ',                         
       '  ! = !/) ',]
n = 9
for i in pin:
    print(i * n)
 
#2
n=0.0
while type (n)!=int:
    try:
        n=int(input("sisestage number, mida ei saa ületada"))
    except:
        TypeError
g=0.0
while type (g) !=int:
    try:
        g=int(input("kraadi"))
    except:
        TypeError
u=0
for i in range(1,n,1):
    u=i**g 
    if u<n:
        print(u)
    else:
        break
print("lõpp\n")

#3 
n=int(input('Sisestage õpilaste arv: '))              #надо написать от 1-10 человек(чтобы долго не писать оценки)
s = 0
for i in range(n):
 a = int(input('Sisesta reiting: '))                  #написать для каждого ученика его оценку
s=s/20.0
s=s+a
print(a)
print("Õpilaste keskmine hinne={0:2f}".format(s))

#4
ameba = 1
time_list = [3,6,9,12,15,18,21,24]
for time in time_list:
   ameba *= 2
   print("Läbi", time ,"tundi saab olema", ameba ," rakud")

