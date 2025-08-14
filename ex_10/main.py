class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_details(self):
      print("-----Détails du Personne-----")
      print("Nom : ", self.name)
      print("Age : ", self.age)

class Employee(Person):
   def __init__(self,name,age,salary):
      super().__init__(name,age)
      self.salary = salary
      
   def display_details(self):
      super().display_details() #appelle la méthode de la class mère
      print("Salaire : ", self.salary)
      

name = input("Entrez le nom :")
age = int(input("Entrez l'Age: "))
salary = float(input("Entrez le salaire: "))

emp = Employee(name,age,salary)
emp.display_details()
