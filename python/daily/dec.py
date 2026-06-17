

def my_dec(func):
    def wrapper(*args, **kwargs):
        print(f"start of the function: {func.__name__} .....")
        result=func(*args, **kwargs)
        print(f"end of this function: {func.__name__}....\n")
        return result
    return wrapper

@my_dec
def add(a,b):
    print(f"adding of {a} and {b} is {a+b}")

@my_dec
def greet(name):
    print(f"Hi {name}, Hava a Nice Day !")

add(5,7)
greet("Kishore")


