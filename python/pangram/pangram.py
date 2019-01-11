def is_pangram(sentence):


    alphaset = frozenset("abcdefghijklmnopqrstuvxyz")
    try:
        while alphaset.issuperset(alphaset.intersection(frozenset(sentence.lower()))):
            return True
        else:
            return False
    except TypeError:
        print("hey now, this isn't a good input")
        raise