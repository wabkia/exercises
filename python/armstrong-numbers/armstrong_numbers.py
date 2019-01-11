def is_armstrong(number):
    # get a length of the number then check Armstrong condition
    # to return true or false
    while isinstance(number, int):
        numberlength = len(str(abs(number)))
        numbersplit = number.split('')
        armstrongtotal = 0
    try:
        for n in numbersplit:
            armstrongtotal += n * numberlength 
        while number == armstrongtotal:
            return
    except:
        print("somethign went wrong, like you didn't give an integer to the function")
        raise
