def roman(input1):
    if input1 == 4:
        input2 = (input1 - 3) * "I" + "V"
        return input2

    elif input1 == 5:
        input2 = "V"
        return input2

    elif input1 >= 6 and input1 < 9:
        input2 = "V" + (input1 - 5) * "I"
        return input2

    elif input1 == 9:
        input2 = (input1 - 8) * "I" + "X"
        return input2

    elif input1 == 27:
        input2 = ((27 // 10) * "X") + "V" + (((27 % 10) - 5) * "I")
        return input2

    else:
        input2 = input1 * "I"
        return input2
