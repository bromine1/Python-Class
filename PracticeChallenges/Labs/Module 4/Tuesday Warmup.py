class Dog:
    def __init__(self, name, age, language = None, occupation = None):
        self.name = name
        self.age = age
        self.language = language
        self.job = occupation
    def description(self):
        return(f"{self.name} is {self.age} years old")


buddy = Dog('Snow White', '3', 'Russian', 'Sewage Manager')
print("Terrierist suspect: \n Name: {name}\n Age: {age}\n Affiliation: {enemy}\n Cover: {job}".format(name = buddy.name, age = buddy.age, enemy = buddy.language, job = buddy.job))
print(buddy.description())