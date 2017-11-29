import json

def graphe_non_orienté1():
    G = dict()
    G["a"] = {"b":6, "c":2}
    G["b"] = {"a": 6, "c": 3}
    G["c"] = {"b": 3, "a": 2}
    return G

print(json.dumps(graphe_non_orienté1()))
texte = open("graphe.json",'w')
texte.write(json.dumps(graphe_non_orienté1(), sort_keys=True, indent=2))
texte.close()

texte = open("graphe.json",'r')
print(type(json.loads(texte.read())))
texte.close()