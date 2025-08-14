def square(x):
    #check if x is an integer or float

    if type(x) == int or type(x) == float:
        return x*x
    else:
        print("Le paramètre doit être nombre.")
        return None
 # Ask the user for input   
user_input = input ("Entrez un nombre : ")

# Try to convert the input to a number
if user_input.isdigit():
    value = int(user_input)
    result = square(value)
    print(f"Le carré de {user_input} : {result}")
else:
    try:
        # Try to convert to float for decimal numbers

        value = float(user_input)
        result = square(value)
        print(f"Le carré de {user_input} : {result}")
    except ValueError:
        # If the conversion fails, calls the function with the original input(string)
        result = square(user_input)

    