def two_fer(name="you"):

    while isinstance(name, str):
    	    return "One for {}, one for me.".format(name)
    else:
    	raise TypeError("You didn't provide a string for a name")