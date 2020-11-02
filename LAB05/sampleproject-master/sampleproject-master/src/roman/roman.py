
def roman(input1):

    if input1 == 4:
        input2 = (input1-3) * "I" + "V"
        return input2

    else:
        input2 = input1*"I"
        return input2
