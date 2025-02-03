# Example Python script with lint issues

def greet(name):
    print(f"Hello, {name}")

def add_numbers(a, b):
    return a + b

greet("Alice")
greet("Bob")

result = add_numbers(5, 10)
print(f"The result is {result}")

def unused_function():
    pass

greet("Charlie")
