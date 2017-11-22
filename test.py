from djisktra import *

def graphe_non_orienté1():
    G = dict()
    G["a"] = {"b":6, "c":2}
    G["b"] = {"a": 6, "c": 3}
    G["c"] = {"b": 3, "a": 2}
    return G


def graphe_non_orienté2():
    G = dict()
    G["a"] = {"b":6, "c":2}
    G["b"] = {"a": 6, "c": 3, "d": 4}
    G["c"] = {"b": 3, "a": 2}
    G["d"] = {"b": 4}
    return G


def graphe_orienté1():
    G = dict()
    G["a"] = {"b":2}
    G["b"] = {"c": 3}
    G["c"] = {"a": 6}
    return G


def graphe_orienté2():
    G = dict()
    G["a"] = {"b": 9, "c": 15, "d":1}
    G["b"] = {"a": 16}
    G["c"] = {"b": 3}
    G["d"] = {"c": 4}
    return G


def test_djikstra1():
    G = graphe_non_orienté1()
    d, prédécesseur = djikstra("a", G)
    assert d["a"] == 0
    assert prédécesseur["a"] == None
    assert d["c"] == 2
    assert prédécesseur["c"] == "a"
    assert d["b"] == 5
    assert prédécesseur["b"] == "c"


def test_djikstra2():
    G = graphe_orienté1()
    d, prédécesseur = djikstra("b", G)
    assert d["b"] == 0
    assert prédécesseur["b"] == None
    assert d["c"] == 3
    assert prédécesseur["c"] == "b"
    assert d["a"] == 9
    assert prédécesseur["a"] == "c"

def test_djikstra3():
    G = graphe_non_orienté2()
    d, prédécesseur = djikstra("a", G)
    assert d["a"] == 0
    assert prédécesseur["a"] == None
    assert d["c"] == 2
    assert prédécesseur["c"] == "a"
    assert d["b"] == 5
    assert prédécesseur["b"] == "c"
    assert d["d"] == 9
    assert prédécesseur["d"] == "b"


def test_djikstra4():
    G = graphe_orienté2()
    d, prédécesseur = djikstra("c", G)
    assert d["c"] == 0
    assert prédécesseur["c"] == None
    assert d["a"] == 19
    assert prédécesseur["a"] == "b"
    assert d["b"] == 3
    assert prédécesseur["b"] == "c"
    assert d["d"] == 20
    assert prédécesseur["d"] == "a"