class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greetingcount = 0

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
        self.greetingcount = self.greetingcount + 1
        return self.greetingcount

    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}")
        print(f"{self.name}'s phone number: {self.phone}.")
    
    def add_friend(self, other):
        friendcounter = 0
        print(f"{self.name}'s friends are: ")
        self.friends.append(other)
        for friend in self.friends:
            friendcounter = friendcounter + 1
            print(f"\n{friendcounter} -- {friend.name.upper()}")
            print(f"{friend.name}'s contact information is: ")
            friend.print_contact_info()
        print("*" * 20)
    
    def numfriends(self):
        return len(self.friends)

    def greeting_count(self):
        return self.greetingcount
    
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
print(jordan.numfriends())
print(jordan.greeting_count())
print(mark.numfriends())