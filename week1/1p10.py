Availible = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
Output = []


def PaymentCalc(Amount, Availible, Output):
    if (Amount < 0):
        return 0
    # if (Amount == 1):
    #     Output.append(1)
    #     Amount-=1

    if (len(Output) >= len(Availible)):
        for i in range(len(Output)):
            if(Output[i] != 0):
                print("%i of %i cents" % (Output[i], Availible[i]))
        return Output
    else:
        if(Amount >= Availible[len(Output)]):
            temp = 0
            for _ in range(0, (Amount / Availible[len(Output)])):
                temp += 1
            Amount = Amount-(temp*Availible[len(Output)])
            Output.append(temp)
            PaymentCalc(Amount, Availible, Output)
        else:
            Output.append(0)
            PaymentCalc(Amount, Availible, Output)


PaymentCalc(372, Availible, Output)
