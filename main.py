"""
This module contains simple functions to demonstrate linting issues and fixes.
"""

def greet(name):
    """
    Print a greeting message to the given name.
    
    Args:
        name (str): The name to greet.
    """
    print(f"Hello, {name}")

def add_numbers(a, b):
    """
    Add two numbers and return the result.
    
    Args:
        a (int): The first number.
        b (int): The second number.
    
    Returns:
        int: The sum of the two numbers.
    """
    return a + b

greet("Alice")
greet("Bob")

result_one = add_numbers(5, 10)
print(f"The result is {result_one}")

greet("Charlie")
