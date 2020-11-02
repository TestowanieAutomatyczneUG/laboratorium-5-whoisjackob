class hamming:

    def distance(self, input1, input2):

        if input1 == "" or input2 == "":

            return 0

        elif len(input1) >= 5 or len(input2) >= 5:

            count = 0
            k = 0

            def check(count, input1, input2, k):

                if k == len(input1):
                    return count
                else:
                    if input1[k] != input2[k]:
                        check(count + 1, input1, input2, k + 1)
                    else:
                        check(count, input1, input2, k + 1)

            check(count, input1, input2, k)

        elif input1 == input2:

            return 0

        elif input1 != input2:

            return 1


