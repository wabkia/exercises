def is_pangram(sentence):


    alphaset = frozenset("abcdefghijklmnopqrstuvxyz")
    try:
        return alphaset.issubset(alphaset.intersection(frozenset(sentence.lower())))
    except TypeError:
        print("hey now, this isn't a good input")
        raise