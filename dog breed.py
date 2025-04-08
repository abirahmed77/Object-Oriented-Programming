class Dog:
    
    animal = "Dog"
    
    def __init__(self, name, age, weight, species, color, angerlevel, origin):
        self.name = name
        self.age = age
        self.weight = weight
        self.species = species
        self.color = color
        self.angerlevel = angerlevel
        self.origin = origin
        
lucky = Dog("Lucky", 5, "32kg", "Boxer", "White and Brown", "Boxers are not naturally aggressive", "Germany")
tiger = Dog("Tiger", 4, "20kg", "German Shepherd", "Black and Brown", "German Shepherds are not inherently aggressive", "Germany")
buddy = Dog("Buddy", 6, "26kgkg", "Bulldog", "White", "Bulldogs are calm and easygoing temperaments", "England")

print(f"Name : {lucky.name}\nAge : {lucky.age}\nWeight : {lucky.weight}\nSpecies : {lucky.species}\nColor : {lucky.angerlevel}\nOrigin : {lucky.origin}")
print()
print()
print(f"Name : {tiger.name}\nAge : {tiger.age}\nWeight : {tiger.weight}\nSpecies : {tiger.species}\nColor : {tiger.angerlevel}\nOrigin : {tiger.origin}")
print()
print()
print(f"Name : {buddy.name}\nAge : {buddy.age}\nWeight : {buddy.weight}\nSpecies : {buddy.species}\nColor : {buddy.angerlevel}\nOrigin : {buddy.origin}")