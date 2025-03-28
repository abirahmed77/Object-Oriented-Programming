class Dog:
    
    animal = "Dog"
    
    def __init__(self, name, age, size, species, color, angerlevel):
        self.name = name
        self.age = age
        self.size = size
        self.species = species
        self.color = color
        self.angerlevel = angerlevel
        
lucky = Dog("Lucky", 4, "110cm", "Boxer", "white", )
rocky = Dog("Woo", 15)
Buddy = Dog("Woo", 15)

print(f"Lucky is a {lucky.species}")