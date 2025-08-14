def log_decorator(func):
    # This function takes another function as input
    def wrapper():
        print("Debut de la fonction.") # Before the original function
        func() # call the original function
        print("Fin de la fonction.") # After the original function
    return wrapper # return the new function
@log_decorator  
def hello():
    print("Bonjour")
# at this point hello = wrapper
hello() # This will run the wrapper, not the original function

