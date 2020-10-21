from math import*
from random import*
import time

x=randint(1,100)
y=randint(1,100)
c=int(input("Saisissez l'abssise de votre bateau"))
z=int(input("Saisissez l'ordonné de votre bateau"))
miss=0
time.sleep(1)
for i in range(5):
    a=int(input('C est à vous !, saisir abscisse'))
    b=int(input('C est à vous !, saisir ordonné'))
    d=sqrt((a-x)**2+(b-y)**2)
    if d < 10:
        print("Bravo vous avez trouvez le bateau!")
        break
    else:
        print(d)
        miss=miss+1
    print("Vous avez raté",miss,"fois")

else:
    print("Le bateau était  a l'emplacement",x,y)
miss1=0
for i in range(5):
    p=randint(1,100)
    o=randint(1,100)
    d1=sqrt((p-c)**2+(o-z)**2)
    if d1 < 10:
        print("Dommage l'ordi a trouvé le bateau, il vas prendre le contrôle du monde maintenant...")
        break
    else:
        print("Ordinateur est à",d1,"mètres de votres bateau")
        miss1=miss1+1
        time.sleep(1)
    print("Ordi a raté",miss1,"fois")
else:
    print("Ordi n'a pas trouvé le bateau a votre emplacement",c,z)

if miss > miss1:
    print("L'ordinateur GAGNE")
if miss==miss1:
    print("Egalité Homme et Machine")
if miss < miss1:
    print("Vous avez Gagner")