contacts_book = {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return "Input Error. Please enter command"
        except SyntaxError as exception:   
            return exception.args[0]
        except TypeError:
            return "Input Error. Please enter command."     
    return inner


def find_comand(user_comand):    
    comand = user_comand
    record = ""
    for key in COMANDS:
        if user_comand.lower().strip().startswith(key):
            comand = key
            record = user_comand[len(key):]
            break
    if record:
        return made_func(comand)(record)
    return made_func(comand)()


def made_func(func):
    return COMANDS.get(func, unknown_func)

def show_all_phone():
    contacts_list = "|{:^10}|{:^15}|".format("Name", "Phone")
    for contact, phone in contacts_book.items():
        contacts_list+= "\n|{:^10}|{:^15}|".format(contact, phone)
    return   contacts_list


def sey_hello():
    return "How can I help you?"


def sey_bye():
    return "Good bye!" 


def unknown_func():
    return "I don't understand what you want. Please enter the correct command"

@input_error
def show_phone(name):
    name = name.strip().split()
    for contact, phone in contacts_book.items():
        if contact == name[0].title() :
            return "|{:^10}|{:^15}|".format(contact, phone)
    raise ValueError("This name is not in the phone book. Please enter the correct name.")


@input_error
def add_phone(phone_line):
    phone_line = phone_line.strip().split(" ")
    name, phone = phone_line[0], phone_line[1]
    if name.title() in contacts_book:
        raise ValueError ("This contact is already in the phone book. Please enter the correct name.")
    elif  not name or not phone:
        raise SyntaxError ("You entered an incorrect phone number or name")
    else:
        contacts_book[name.title()] = phone
        return f"{name.title()}'s phone added to the phone book."


@input_error
def change_phone(phone_line):
    phone_line = phone_line.strip().split(" ")
    name, phone = phone_line[0], phone_line[1]
    if name.title() in contacts_book: 
        contacts_book[name.title()] = phone
        return f"{name.title()}'s phone number has been changed"
    else:
        raise ValueError ("This contact is not in the phone book. Please enter the correct name.")


COMANDS = {
        "hello": sey_hello,
        "add" : add_phone,
        "change" : change_phone,
        "phone" : show_phone,
        "show all": show_all_phone,
        "good bye": sey_bye, 
        "close": sey_bye,
        "end": sey_bye
        }

            
def main():
    while True:
        user_comand = input("... ")
        result = find_comand(user_comand)
        print(result)
        if result == "Good bye!":
            break


if __name__ == '__main__':
    main()
    