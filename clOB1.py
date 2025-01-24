class person:
    #this function __init__ is a constructor of class,
    #self represents the object on which the method is being called
    #a constructor is a function which is called when an object is created of any class
    #a constructor is a special method within a class that is automatically called when an object of that class is created. 
    def __init__(self,name,occupation):
        self.name=name
        self.occupation=occupation
        
    #now lets create a function which can display name and occupation of any object
    def show(self):
        print("name=",self.name)
        print("occupation=",self.occupation)
    
    
#creating two constructore a and b with name and occ as their argument in constructor
a=person("vinay","student")#here  a is being passed as self 
b=person("rsc","student")#and here self represent b

print(a)
print(b)#printing object directly shows the memory location 

print(a.name,a.occupation)#these are the method to access name and occupation from class
print(b.name,b.occupation)#these are the method to access name and occupation from class
print()
print()

#now lets display name and occ using show function of class person
#syntax:object.function_name(list_of argument(optional))
a.show()#you can call a class function by this 
#output
#name=
#occupation=student
b.show()
#output
#name=rsc
#occupation=student

        