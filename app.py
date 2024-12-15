# app.py

def greet(name):
    """Function to greet the user"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))

