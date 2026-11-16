# Version 5.0 - Ticket: PROJ-101
def greet(name="World", lang="en"):
    greetings = {
        "en": "Hello",
        "es": "Hola",
        "hi": "Namaste"
    }
    prefix = greetings.get(lang, "Hello")
    print(f"{prefix}, {name}!")

greet("Pratyaksh", lang="en")
greet("Pratyaksh", lang="hi")
