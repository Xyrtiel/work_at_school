'''
Un triangle coloré est créé à partir d’une rangée de couleurs, chacune étant rouge, verte ou bleue. Rangées successives,
chacune contenant une couleur de moins que la dernière, sont générées en considérant les deux couleurs qui se touchent 
dans le ou la rangée précédente. Si ces couleurs sont identiques, la même couleur est utilisée dans la nouvelle rangée. 
S’ils sont différents, la couleur manquante est utilisée dans la nouvelle ligne. Cette opération se poursuit 
jusqu’à ce que la dernière ligne, avec une seule couleur, soit générée.

Les différentes possibilités sont :

Couleur ici:            G G        B G        R G        B R
Devient la couleur:      G          R          B          G
'''

# VERSION SIMPLE

def triange(string, row):
    for _ in range(row):
        new_liste_color = ""
        for i in range(len(string) - 1):
            color_a = string[i]
            color_b = string[i + 1]
            # Mise en place des combinaisons de couleur pour le Rouge :
            if color_a == "R" and color_b == "R":
                color_c = "R"
            elif color_a == "R" and color_b == "G":
                color_c = "B"
            elif color_a == "R" and color_b == "B":
                color_c = "G"
            # Mise en place des combinaisons de couleur pour le Vert :
            elif color_a == "G" and color_b == "G":
                color_c = "G"
            elif color_a == "G" and color_b == "R":
                color_c = "B"
            elif color_a == "G" and color_b == "B":
                color_c = "R"
            # Mise en place des combinaisons de couleur pour le Bleu :
            elif color_a == "B" and color_b == "B":
                color_c = "B"
            elif color_a == "B" and color_b == "G":
                color_c = "R"
            elif color_a == "B" and color_b == "R":
                color_c = "G"
            new_liste_color += color_c
        string = new_liste_color  # Met à jour la chaîne pour la prochaine itération

    print(new_liste_color, "\n")

triange("RRGGRR", 5)

# VERSION COMPLIQUEE

def triangle(string):
    def get_next_color(color_a, color_b):
        if color_a == color_b:
            return color_a
        # Retourner la couleur qui n'est pas dans color_a et color_b
        return {'R', 'G', 'B'}.difference([color_a, color_b]).pop()

    # Réduire la chaîne jusqu'à ce qu'il ne reste qu'une couleur
    while len(string) > 1:
        new_liste_color = ""
        for i in range(len(string) - 1):
            color_a = string[i]
            color_b = string[i + 1]
            new_liste_color += get_next_color(color_a, color_b)
        string = new_liste_color  # Mettre à jour la chaîne avec la nouvelle ligne

    return string

# VERSION HYPER COMPLIQUEE

COLORS = set("RGB")
def triangle(row):
    while len(row)>1:
        row = ''.join( a if a==b else (COLORS-{a,b}).pop() for a,b in zip(row, row[1:]))
    return row