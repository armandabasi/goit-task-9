def input_error(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ValueError:
            print("Name entered incorrectly.")
        except IndexError:
            print("Invalid input format.")
        except SyntaxError:   
            print("Please enter name and phone number.")
    return inner


def show_all_phone(contacts_book):
    print("|{:^10}|{:^15}|".format("Name", "Phone"))
    for contact, phone in contacts_book.items():
        print("|{:^10}|{:^15}|".format(contact, phone))    

@input_error
def show_phone(name):
    if len(name) != 2:
        raise IndexError("Give me name")
    for contact, phone in contacts_book.items():
        if contact == name[1].title() :
            return print("|{:^10}|{:^15}|".format(contact, phone))
    raise ValueError("This name is not in the phone book. Please enter the correct name.")

@input_error
def add_phone(phone_line):
    if len(phone_line) != 3:
        raise IndexError("Give me name and phone please")
    elif phone_line[1].title() in contacts_book:
        raise ValueError ("This contact is already in the phone book. Please enter the correct name.")
    elif  not phone_line[1] or not phone_line[2]:
        raise SyntaxError ("You entered an incorrect phone number or name")
    else:
        contacts_book[phone_line[1].title()] = phone_line[2]

@input_error
def change_phone(phone_line):
    if len(phone_line) != 3:
        raise IndexError("Give me name and phone please")
    elif phone_line[1].title() in contacts_book: 
        contacts_book[phone_line[1].title()] = phone_line[2]
    else:
        raise ValueError ("This contact is not in the phone book. Please enter the correct name.")
            
def main():
    global contacts_book
    contacts_book = {}
    shutdown_commands = ["good bye", "close", "end"]
    comands = {
        "add" : add_phone,
        "change" : change_phone,
        "phone" : show_phone
    }
    while True:
        user_comand = input("... ").lower()
        if user_comand == "hello":
            print("How can I help you?")
        elif user_comand in shutdown_commands:
            print("Good bye!")
            break
        elif user_comand == "show all":
            show_all_phone(contacts_book)
        else:
            user_comand = user_comand.split(" ")
            if user_comand[0] in comands:
                comands[user_comand[0]](user_comand)

if __name__ == '__main__':
    main()
    