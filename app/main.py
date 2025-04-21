from termcolor import cprint

from package.hello import say_hi


def greet():
    response = say_hi()
    return f"The Python package says, '{response}'"

if __name__ == "__main__":
   cprint(greet(), "red", attrs=["bold"])