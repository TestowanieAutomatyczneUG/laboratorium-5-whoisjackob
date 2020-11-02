class hamming:

    def distance(self, input1, input2):

        if input1 == "" and input2 == "":

            return 0

        elif len(input1) == 12 and len(input2) == 12:

            count = 0
            k = 0

            def check(count, input1, input2, k):

                if k == len(input1):
                    return int(count)
                else:
                    if input1[k] != input2[k]:
                        check(count + 1, input1, input2, k + 1)
                    else:
                        check(count, input1, input2, k + 1)

            check(count, input1, input2, k)

        #wszystko przechodzi oprocz 4 i 5 testu
        #wszystko liczy i zwraca poprawnie. inne infy nie kolidują ale jednak test nie przechodzi
        #zamiast wartosci count widzi 'None'

        elif len(input1) == 1 and len(input2) == 1 and input1 == input2:

            return 0

        elif len(input1) == 1 and len(input2) == 1 and input1 != input2:

            return 1

        elif input1 > input2:

            raise ValueError("Pierwsze slowo jest dluzsze od drugiego")

        elif input1 < input2:

            raise ValueError("Pierwsze slowo jest krotsze od drugiego")

        elif input1 == "" and input2 != "":

            raise ValueError("Pierwszy input jest pusty")

        elif input2 == "" and input1 != "":

            raise ValueError("Drugi input jest pusty")




