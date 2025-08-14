class BankAccount:
    def __init__(self, account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}£ déposée sur le compte.")
        else:
            print(f"Le montant du dépot doit être positif.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Fonds insuffisants pour ce retrait")
        elif amount <= 0:
            print("Le montant du retrait doit etre positif.")
        else:
            self.balance -= amount
            print(f"{amount}£ retirés du compte.")

    def display_balance(self):
        print("------Détails------")
        print("Titulaire du compte :",self.account_holder)
        print("Solde Actuel : ", self.balance, "£")

nom = input("Entrez le nom du titulaire du compte : ")
solde_initial = float(input("Entrez le solde initial: "))

compte = BankAccount(nom, solde_initial)

compte.display_balance()
compte.deposit(float(input("Montant à déposer : ")))
compte.display_balance()
compte.withdraw(float(input("Montant à retirer : ")))
compte.display_balance()


        


  