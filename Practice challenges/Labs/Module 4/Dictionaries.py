# Ryan Stauffer Dictionary Practice

# Create Class because I'm extra
class person:
    def __init__(self, first_name, last_name, age, city ) -> None:
        self.profile = {'first_name' : first_name, 'last_name' : last_name, 'age' : age, 'city' : city}

# Cole Example
person1 = person('Cole', 'Kaupang', '16', 'Cary',)
print(person1.profile['first_name'])
print(person1.profile['last_name'])
print(person1.profile['age'])
print(person1.profile['city'])

# Get user input
firstName = input("Please enter the subject's first name")
LastName = input("Please enter the subjects last name")
Age = input("Please enter the subjects age")
City = input(" Please input the subject's city")

# Retive user defined person
person2 = person(firstName, LastName, Age, City )
print(person2.profile['first_name'])
print(person2.profile['last_name'])
print(person2.profile['age'])
print(person2.profile['city'])