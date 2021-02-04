#We will be creating a calculator that will be performing this four basic functions
# -Addition
# -Subtraction
# -Division
# -multiplication

class Calculator:
    def AdditionMethod(self, a, b):
        additionResult = a + b
        return additionResult
    
    def DivisionMethod(self, a, b):
        divisionresult = a / b
        return divisionresult

    def SubtractionMethod(self, a, b,):
        subtractionresult = a - b
        return subtractionresult

    def MultiplicationMethod (self, a, b):
        multiplicationresult = a * b
        return multiplicationresult



def main():
    firstVal = int(input("Input fIrst value: \t"))
    secondval = int(input("Input second value: \t"))
    print("\n Input which operation to perform \n")
    print("1 - Addition \n 2 - Division \n 3 - Subtraction \n 4 - Multiplication")
    option = int(input("Select Option: "))
    if(option == 1):
        result = Calculator().AdditionMethod(firstVal, secondval)
        print("Addition of ", firstVal, " and ", secondval, " is ", result)
    elif(option == 2):
        result = Calculator().DivisionMethod(firstVal, secondval)
        print(firstVal, " divided by ", secondval, " equals to ", result)
    elif(option == 3):
        result = Calculator().SubtractionMethod(firstVal, secondval)
        print(" Subtraction of ", firstVal, "and", secondval, " equals to ", result)
    elif(option == 4):
        result = Calculator().MultiplicationMethod(firstVal, secondval)
        print ( firstVal, " multiplied by ", secondval, " equals to ", result)
    else:
        print("Invalid option selected")
    

if __name__ == "__main__":
    main()

