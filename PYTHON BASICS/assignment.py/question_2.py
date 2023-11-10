#object oriented programming is a computer programing model that organises software design around data, or objects, rather than functions and logic.
#advantages
#trouble shooting is easy
#solves problems
#security
#productivity

#class is a template definition of the methods and variables in a particular kind of object

#object is a combination of variables,functions,and data structures

#create a user class with properties name,age,location

class person:
    def _init_(self.name,age,location):
        self.name = name
        self.age = age
         self.location = location
        
        person1 = person("Racheal",22, "Kabale") 

        print(person1.name)
        print(personl.age)
        print(personl.location)

        #create a new instance of the user class (a new object)
        person2 = person("richard", 30, "Mbarara")
                         
        print(person2.name)
        print(person2.age)
        print(person2.location)

#access the user name and age
person=person1.name
person=person1.age

print(f 'user name: {person1.name}1)')
print(f'age: (person2.age)')

#create a function for the class  that printss a user's location 
def my_location(my):
   print('my location: ', my)
my_location('kabale') 