from Prim import *

def graphe1():
    g= dict()
    g["a"] = {"b":4 , "c":5}
    g["b"] = {"a": 4, "c": 3}
    g["c"] = {"a": 5, "b": 4, "d":1}
    g["d"] = {"c": 1}
    return g

def test_Prim1():
    g = graphe1()
    d, pred = prim("a", g)
    assert pred["b"] == "a"
    assert pred["c"] == "b"
    assert pred["d"] == "c"
