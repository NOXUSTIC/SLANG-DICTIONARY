import json

def load_slang_dictionary():
    try:
        with open('slang_dictionary.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_slang_dictionary(slang_dictionary):
    with open('slang_dictionary.json', 'w') as file:
        json.dump(slang_dictionary, file)

def add_slang(slang, origin):
    slang = slang.lower()
    if slang not in slang_dictionary:
        slang_dictionary[slang] = origin.lower()
        print(f"Slang '{slang}' added with origin '{origin}'.")
        save_slang_dictionary(slang_dictionary)
    else:
        print("Slang already exists.")

def get_slang_origin(slang):
    slang = slang.lower()
    if slang in slang_dictionary:
        return slang_dictionary[slang]
    else:
        return "Slang not found."

def remove_slang(slang):
    slang = slang.lower()
    if slang in slang_dictionary:
        origin = slang_dictionary.pop(slang)
        print(f"Slang '{slang}' with origin '{origin}' removed.")
        save_slang_dictionary(slang_dictionary)
    else:
        print("Slang not found.")

def remove_all():
    slang_dictionary.clear()
    save_slang_dictionary(slang_dictionary)
    print("All slangs and their origins removed.")

def check_all():
    origins = set(slang_dictionary.values())
    for origin in origins:
        print(f"The origin is {origin}")
        print()
        print(f"The slangs under this origin are:")
        print()
        for slang, origin_value in slang_dictionary.items():
            if origin_value == origin:
                print(f"{slang}")
        print()

        

# Load existing slang dictionary or initialize a new one
slang_dictionary = load_slang_dictionary()
while True:
    command = input("Enter a command (add, origin, remove, quit, check all, remove all): ")

    if command == "add":
        slang = input("Enter the slang: ").lower()
        origin = input("Enter the origin: ").lower()
        add_slang(slang, origin)
    elif command == "origin":
        slang = input("Enter the slang: ")
        origin = get_slang_origin(slang)
        print(f"The origin of '{slang}' is '{origin}'.")
    elif command == "remove":
        slang = input("Enter the slang: ")
        remove_slang(slang)
    elif command == "check all":
        check_all()
    elif command == "remove all":
        remove_all()
    elif command == "quit":
        break
    else:
        print("Invalid command.")
        

print("Exiting the program.")

    
