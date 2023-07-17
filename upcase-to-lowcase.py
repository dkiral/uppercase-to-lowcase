fichier_entree = input("Veuillez fournir le chemin du fichier d'entrée : ")

try:
    with open(fichier_entree, "r") as f_entree:
        contenu = f_entree.read()
except FileNotFoundError:
    print("Le fichier d'entrée n'existe pas.")
    exit()

contenu_minuscules = contenu.lower()

fichier_sortie = "output.txt"

with open(fichier_sortie, "w") as f_sortie:
    f_sortie.write(contenu_minuscules)

print("Conversion terminée !")