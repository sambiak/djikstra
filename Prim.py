from urllib.request import urlopen
import json
import string

def prim(racine, graphe):
    exploré = {racine}
    d = {racine: 0}
    prédécesseur = {racine: None}
    pivot = racine
    for i in range(len(graphe) - 1):
        for voisin in graphe[pivot].keys():
            if voisin not in exploré:
                if voisin not in d.keys() or graphe[pivot][voisin] < d[voisin]:
                    d[voisin] = graphe[pivot][voisin]
                    prédécesseur[voisin] = pivot

        minimum = None
        for s in d.keys():
            if s not in exploré:
                if minimum == None or d[s] < minimum:
                    minimum = d[s]
                    pivot = s
        exploré.add(pivot)
    return d, prédécesseur

villes = ["Mans,Belgium", "Bruyes,Belgium", "Bruxelles,Belgium", "Anvers,Belgium", "Namur,Belgium", "Lieje,Belgium", "Arlan,Belgium"]

origin = ""
for i, ville in enumerate(villes):
    if i == 0:
        origin += ville
    else:
        origin += "|" + ville
print(origin)

key = "%20AIzaSyCCjU5nzk7PLRkBtn9vH3yPx7YoXauPB3o"
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=standard&origins=" + origin + "&destinations=" + origin + "&key=" + key
print(url)
donnees = urlopen(url)
str_response = donnees.read().decode('utf-8')
print(json.loads(str_response)['rows'])

liste_de_elements = json.loads(str_response)['rows']

G = dict()
for i, ville in enumerate(villes):
    G[ville] = dict()
    for j, dest_ville in enumerate(liste_de_elements[i]["elements"]):
        if i != j:
            G[ville][villes[j]] = dest_ville["duration"]["value"]
print(G)
print(prim("Mans,Belgium", G))

#donnees = urlopen("""https://maps.googleapis.com/maps/api/distancematrix/json?units=standard&origins=Washington,DC&destinations=New+York+City,NY&key=%20AIzaSyCCjU5nzk7PLRkBtn9vH3yPx7YoXauPB3o""",None)
#str_response = donnees.read().decode('utf-8')
#print(json.loads(str_response)['rows']['elements']['duration']['value'])