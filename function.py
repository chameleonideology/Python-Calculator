def add(param1, param2):
    num1= param1
    num2= param2
    addition = int(num1) + int(num2)
    print (addition)

def calculator():
    num1 = input('what is your first number?')
    num2 = input('what is your second number?')
    name = input ('whats your name')
    add(num1, num2)



    #concatenation of string
    #"2" + "7" = "27" it will add the number together but not in mathmatcal orders.
    #but in other to chnage the data(data conversion) type you wrap your data in "int"

    
    print(f"you are beautiful {name}")

def main():
    pass   

calculator()
