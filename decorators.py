#Decorators
def decorated_function(orignal_function):
    def wrapper_function():
        print('Wrapper function executed before {}'.format(orignal_function.__name__))
        return orignal_function()
    return wrapper_function

def display():
    print('Display function using function as decorator')

decorated_var = decorated_function(display)
decorated_var()
#  Another way
def outer(original):
    def inner(*args, **kargs):
        print('Inner executed before {}'.format(original.__name__))
        return original(*args, **kargs)
    return inner
@outer
def display1():
    print("display function using decorator as funtion and using @outer")

@outer
def display_info(name,age):
    print("Name and age: {} {}".format(name,age))    

display1()
display_info('Ramsha',19)
 
 #decorator using class
class decorator_class(object):
   def __init__(self,orignal_function):
      self.orignal_function = orignal_function
   def __call__(self,*args,**kwargs):
      return self.orignal_function(*args,**kwargs)
@decorator_class
def display2():
    print("This is display function using class as decorator")
@decorator_class
def display_info1(name,age):
    print('Name = {} , Age = {}'.format(name,age))
display2()
display_info1('Ramsha', 19)