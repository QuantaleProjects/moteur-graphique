import time

longueur, largeur = 237,63 - 1
image = [[' ' for _ in range(longueur)] for _ in range(largeur)]

def placerPixel(x,y,char):
    x1=round(x)
    y1=round(y)
    if 0<=x1<=longueur-1 and 0<=y1<=largeur-1:
        image[y1][x1]=char

def afficher():
    strImage=' '*longueur
    for y in range(largeur):
        for x in range(longueur):
            strImage+=image[y][x]
    print(strImage,end='')

def supprimer():
    for y in range(largeur):
        for x in range(longueur):
            image[y][x]=' '

dernier = time.time()

while True:
    actuelle = time.time()
    dt=actuelle-dernier
    dernier = actuelle
    supprimer()
    
    placerPixel(longueur//2,largeur//2,'#')

    afficher()
