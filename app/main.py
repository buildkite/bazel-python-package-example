from package.hello import say_hi

def greet():
    response = say_hi()
    return f"The Python package says, '{response}'"


print(greet())
