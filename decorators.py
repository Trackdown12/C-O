"""
this will show how decorators are made 

Decorators-> decorators are the function which take another function as an argument and 
modifies it or decorates it

"""


#this is a decorator
#decorating a function having no argument
def greetmorn(fx):
    def greet():
        print("hello good morning")
        fx()
        print("thanks for waiting")
    return greet
@greetmorn
def name():
    x=input("enter your name please: ")
    print(x)




def greeteve(fx):
    """
    this is a decorator which will have arguments 
    Args:
        fx (_type_=function): greeteve contains function as an argument
    """
    def greet(*args,**kwargs):
        print("hello good morning")
        fx(*args,**kwargs)
        print("thanks for waiting")
    return greet

@greeteve
def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
