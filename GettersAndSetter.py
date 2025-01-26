"""
getters:
get the value
setters:
set the value
getters and setters are methods that provide controlled access to the attributes of a class. 

Public: Attributes and methods without leading underscores are public and accessible from anywhere.   

Protected: Attributes and methods with a single leading underscore are conventionally considered protected, intended for use within the class and its subclasses.   

Private: Attributes and methods with double leading underscores undergo name mangling, making them harder to access from outside the class.

getters and setters provide flexibility to class and also prevents data from  gettin unneceassary change or access 
"""
#normal class
class name:
    def __init__(self,name):
        self.__private_name=name# NOW VARIABLE self._name is private data
        self._protected_name=name# NOW VARIABLE self._name is protected data
        self.publicname=name# NOW VARIABLE self._name is public data
    
    def name(self):
        return self.__private_name
a=name("vinay")
#belowline causes error cause cannot  access private data outside the class
# print(a.__private_name)
print(a._protected_name)#output:vinay but discouraged as protected item can be accessed but we should not access it {bad practice}
print(a.publicname)##output:vinay we can access public variable directly
print(a.name())#output:vinay accessing private data using function

a._protected_name="vk" #we can access and change protected data but it is generally discouraged as python do not strictly encapsulates by using access specifier
a.publicname="v k"
print(f"protected data={a._protected_name}")
print(f"public data={a.publicname}")


class employee:
    def __init__(self,name,id):
        self.__private_name=name
        self.__private_id=id
    
    #property is actually a decorator
    @property#this enhances encapsulation in python class
    def sdata(self):
        return self.__private_name.capitalize(),self.__private_id
    #property make data look like directly accessible but its not
    
    
    #setter
    #setter is expecting tuple as an argument so we need to use index for assigning multiple values
    @sdata.setter
    def sdata(self,new_data):
        print(type(new_data))
        self.__private_name=new_data[0]
        self.__private_id=new_data[1]
    
b=employee("suraj",2001)
name_emp,id=b.sdata#its a function but it is written like a variable which enhances encapsulation
print(f"name of employee={name_emp}")
print(f"id of employee={id}")


#now if you try to change data using getter here{b.show} u can not do it as it will give attribute error
#so we need to define a setter so that we can set value for different object of classes

#we have defined setter in python which requires same name as getter for readability and consistency
#name_emp and id consist data of object a


b.sdata = "vipin", 200 #argument wi be considered a tuple by setter
name_emp, id = b.sdata # Update the variables after setting the new values

print(f"name of employee={name_emp}")
print(f"id of employee={id}")

#output
#name of employee=Vipin
#id of employee=200
#now you can see that output for same object b has been changed using setter which was not possible or discouraged