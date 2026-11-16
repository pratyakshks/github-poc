# Version 4.0 - Ticket: PROJ-101
def greet(name="World", uppercase=False):
    message = f"Hello, {name}!"
    print(message.upper() if uppercase else message)

greet("GitHub User")
greet("GitHub User", uppercase=True)
