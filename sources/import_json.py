import json

with open('data/niveau.json', 'r',encoding="utf-8") as file:
    data = json.load(file)#importe le dict json sous le nom de data
"""
for i in range(len(data["niveau"])):
    print(data["niveau"][i]["nom"])#affiche le nom de la molecule
    print(data["niveau"][i]["formule brute"])
    print(data["niveau"][i]["atomes"])
    for j in data["niveau"][i]["atomes"]:
        print(j)
    print("")
"""
with open('data/atome.json', 'r',encoding="utf-8") as fichier:
    donnee = json.load(fichier)

for i in range(len(donnee["atome"])):
    print(donnee["atome"][i]["symbole"])#affiche le nom de la molecule
    print(donnee["atome"][i]["nom"])
    print(donnee["atome"][i]["valence"])
    print(donnee["atome"][i]["couleur"])
    print(donnee["atome"][i]["rayon"])
    

    print("")
