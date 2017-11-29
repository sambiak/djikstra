from Prim import *

def graphe1():
    g= dict()
    g["a"] = {"b":4 , "c":5}
    g["b"] = {"a": 4, "c": 3}
    g["c"] = {"a": 5, "b": 4, "d":1}
    g["d"] = {"c": 1}
    return g

def graphe2():
    G = dict()
    G["a"] = {"b":6, "c":2}
    G["b"] = {"a": 6, "c": 3}
    G["c"] = {"b": 3, "a": 2}
    return G

def test_Prim1():
    g = graphe1()
    d, pred = prim("a", g)
    assert pred["b"] == "a"
    assert pred["c"] == "b"
    assert pred["d"] == "c"
    assert d["b"] == 4
    assert d["c"] == 3
    assert d["d"] == 1

def test_Prim2():
    g = graphe2()
    d, pred = prim("a", g)
    assert pred["b"] == "c"
    assert pred["c"] == "a"
