def is_armstrong(number):
    # get a length of the number then check Armstrong condition
    # to return true or false
    numberlength = len(str(abs(number)))
    numbersplit = number.split('')
    armstrongtotal = 0
    try:
        for n in numbersplit:
            armstrongtotal += n * numberlength 
        while number == armstrongtotal:
            return
