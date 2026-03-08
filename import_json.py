import json

with open('molecules.json', 'r',encoding="utf-8") as file:
    data = json.load(file)#importe le dict json sous le nom de data

for i in range(len(data["molecules"])):
    print(data["molecules"][i]["nom"])#affiche le nom de la molecule
    print(data["molecules"][i]["formule brute"])
    print(data["molecules"][i]["atomes"])
    for j in data["molecules"][i]["atomes"]:
        print(j)
    print("")