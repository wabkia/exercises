def is_armstrong(number):
    # get a length of the number then check Armstrong condition
    # to return true or false
    while isinstance(number, int):
        numberlength = int(len(str(abs(number))))
        numbersplit = [int(str(number)[i:i+1]) for i in range(0, len(str(number)), 1)]
        armstrongtotal = 0

        try:
            for n in numbersplit:
                armstrongtotal += n ** numberlength
            return number == armstrongtotal
        except:
            print("something went wrong, like you didn't give an integer to the function")
            raise
