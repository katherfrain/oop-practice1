class Person:
    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone
         self.friends = []


    def greet(self, other_person):
         print('Hello {}, I am {}!'.format(other_person.name, self.name)) 
    
    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}\n{self.name}'s phone number: {self.phone}.")
    
    def add_friend(self, other):
        self.friends.append(other)
        for friend in self.friends:
            print(friend.name)
    
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
mark = Person("Mark", "mark@markmail.com", "911")

Person.greet(sonny, jordan)
Person.greet(jordan, sonny)

print("Sonny's email is", sonny.email)
print("Jordan's contact info is:", jordan.email, jordan.phone)
sonny.print_contact_info()

jordan.add_friend(sonny)
jordan.add_friend(mark)