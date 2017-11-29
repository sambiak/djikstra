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


donnees = urlopen("""https://maps.googleapis.com/maps/api/distancematrix/json?units=standard&origins=Washington,DC&destinations=New+York+City,NY&key=%20AIzaSyCCjU5nzk7PLRkBtn9vH3yPx7YoXauPB3o""",None)
str_response = donnees.read().decode('utf-8')
print(json.loads(str_response))