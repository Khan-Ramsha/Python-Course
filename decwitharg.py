# def prefix_decorator(prefix):
#     def decorator_function(original_function):
#         def wrapper_function(*args,**kwargs):
#             print(prefix,'Executed before {}'.format(original_function.__name__))
#             result = original_function(*args,**kwargs)
#             print(prefix,'Executed after {}'.format(original_function.__name__))
#             return result
#         return wrapper_function
#     return decorator_function
# @prefix_decorator('TESTTING:')
# def display_info(name,age):
#     print('Age={},Name={}'.format(name,age))
# display_info(19,'Ramsha')
# def uppercase_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
    
#         return result.upper()
#         return result
#     return wrapper

# @uppercase_decorator
# def greet(name):
#     return f"Hello, {name}!"

# @uppercase_decorator
# def echo(text):
#     return text

# print(greet("John")) # Output: HELLO, JOHN!
def prefix_decorator(pre):
    def decorator_function(text):
        def wrapper_function(*args):
            print(pre,'{} Executed before {}'.format(wrapper_function.__name__,text.__name__))
            result = text(*args)
            return result.upper()
        return wrapper_function
    return decorator_function
@prefix_decorator('UPPERCASE CONVERSION:')
def display(name):
     return 'hello {}'.format(name)   ##  return f"Hello, {name}!"
print(display('John'))
