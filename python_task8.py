import pyjokes
import turtle
from turtle import *

print("- TACHE 1 -")

print(pyjokes.get_joke("en", "chuck"))
print("----------------------------------")

print("- TACHE 2 -")

# 2.1
''' from turtle import * '''

for i in range(0, 4):
    forward(100)
    left(90)
print("Je viens de dessiner un carré en utilisant une boucle.")

# 2.2 
'''
toto = turtle.Screen ()
toto.bgcolor("black")
titi = turtle.Turtle ()
titi.color("red")
for i in range (3) :
    titi.right (90)
    titi.circle (42)
toto.exitonclick ()
'''

# 2.3
'''
def draw_polygon(sides):
    for i in range(0, sides):
        forward(100)
        left(360/sides)

nombre_cotes = int(input("Combien voulez vous de côtés à la forme que vous souhaitez représenter ? = "))
draw_polygon(nombre_cotes)
'''

# 2.4
'''
turtle = turtle.Turtle()
r = 1

for i in range(100):
    turtle.circle(r + i, 50)
'''

# CHALLENGES :
# CHALLENGE 1 :
'''
import turtle
import random

scrin = turtle.Screen()
scrin.colormode(255)  # On passe en mode RGB pour des couleurs en valeurs 0-255
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Boucle pour dessiner une spirale de carrés avec des rotations et des couleurs aléatoires
for i in range(75):  # Ajuste le nombre pour obtenir plus ou moins de carrés
    # Génère des couleurs aléatoires pour le contour et le remplissage
    r_contour = random.randint(0, 255)
    g_contour = random.randint(0, 255)
    b_contour = random.randint(0, 255)

    r_fill = random.randint(0, 255)
    g_fill = random.randint(0, 255)
    b_fill = random.randint(0, 255)
    
    t.color((r_contour, g_contour, b_contour))  # Applique la couleur du contour
    t.fillcolor((r_fill, g_fill, b_fill))  # Applique la couleur de remplissage
    
    t.begin_fill()  # Commence le remplissage
    for _ in range(4):
        t.forward(10 + i*5)  # Augmente la taille du carré à chaque itération
        t.left(90)
    t.end_fill()  # Termine le remplissage
    
    t.left(15)  # Tourne légèrement la tortue pour chaque nouveau carré

scrin.exitonclick()
'''

# CHALLENGE 2
'''
import turtle
import random
import math

turtle.speed(100000000000000000000000000000000000)
turtle.color("black")
turtle.up()

phi = (1 + math.sqrt(5)) / 2
i = 360 / math.pi * phi
t = turtle
distance = 100  # Distance initiale à avancer
scale = 0.5
turtle.pendown()  # Reprendre le dessin

for x in range(900):
    turtle.forward(distance)  # Avancer d'une certaine distance
    turtle.right(i)  # Tourner à droite
    distance += scale  # Augmenter la distance à chaque itération
'''

print("- TACHE 3 - ")

# 3.1