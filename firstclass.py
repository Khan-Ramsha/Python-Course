#First class function
# Python program to illustrate functions
# Functions can return another function
def outer():
   print('Hello, from outer')
   def inner():
      print("Hello from inner!")
   return inner
var = outer()
var()

def outer1(x):
   
   def inner1(y):
     return x+y
   return inner1

var1 = outer1(20)
print(var1(11))