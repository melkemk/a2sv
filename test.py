def hello(name):
    return "Hello " + name

def test():
    assert hello("Nahom") == "Hello Nahom"
    assert hello("Nahom") != "Hello"