class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_area(self):
        return self.width * self.length
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.length)
    
width_input = input ("Entrez la largeur du rectangle : ")
width = float(width_input)
length_input = input ("Entrez la longeur du rectangle : ")
length = float(length_input)


 #créer un objet Rectangle
rect = Rectangle(width, length)

print("Aire du rectangle : ",rect.calculate_area())   
print("Périmètre du rectange : ", rect.calculate_perimeter()) 

    
