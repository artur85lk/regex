import re


def engine(x):

    text = x.split("|")
    o = True
    if re.search(text[0], text[1]):
        o = True
    else:
        o = False
    print(f"{o}")
x = input()
engine(x)

def test_e():

    assert engine("^apple$|tasty apple") == False
