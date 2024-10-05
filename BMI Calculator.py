#BMi Calculator =(weight in pounds x 703) / (height in inches x height in inches)


def BMI():
    name = str(input('Enter your name:  '))
    weight = int(input('Enter your weight in pound: '))
    height = int(input('Enter your height in inches:  '))

    BMi = (weight * 703) / (height * height )

    print(BMi)

    if BMi >0:

        if BMi >= 18.5 or BMi <= 24.9:
            print(name +' You are underweight or your weight is Normal')

        elif  BMi >= 29.9:
            print(name + ' You are Overweight')
        elif  BMi >= 34.9:
            print(name + " obese----> High")
        elif BMi >= 35:
            print(name + ' Severely Obese---> Very Heigh')
        elif BMi >= 40:
            print(name +' Over-Morbidly Obese --> Extremely Heigh')

    else:
        print(' Enter valid Inputs for weight and height ')

    

BMI()













