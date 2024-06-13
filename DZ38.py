
import json

# Телефонная книга
contacts = {}

# Главное меню
def phone_book():
    while True:
        print("\n 1 - Просмотр телефонной книги")
        print("\n 2 - Создание контакта")
        print("\n 3 - Изменение контакта")
        print("\n 4 - Поиск контакта")
        print("\n 5 - Удаление контакта")
        print("\n 6 - Выход")
        print("\n")
 
        menu_item = input()
 
        if menu_item == "1":
            show_phonebook()
        elif menu_item == "2":
            create_contact()
        elif menu_item == "3":
            edit_contact()
        elif menu_item == "4":
            print("\n поиск по номеру телефона")
            find_contact()
        elif menu_item == "5":
            print("\n Введите номер телефона")
            delete_contact()
        elif menu_item == "6":
            break
        else:
            print("\n Введите номер пункта меню из списка")

# Просмотр телефонной книги
def show_phonebook():
    if len(contacts) != 0:
        for phone, name in contacts.items():
            print(f"\n {phone} - {name}")
    else:
        print("\n Нет записей")

# Создание контакта
def create_contact():
    print("\n")
    phone = input("Номер - ")
    first_name = input("Имя - ")
    last_name = input("Фамилия - ")
    contacts[phone] = first_name + " " + last_name
    save_phonebook()
    print(f"\n Контакт {first_name} {last_name} добавлен.")

# Изменеение конакта
def edit_contact():
    print("\n")
    contact = input("Номер - ") 
    if contact in contacts:
        print(f"\n {contact}: {contacts[contact]}")
        first_name = input("Новое имя - ")
        last_name = input("Новая фамилия - ")
        contacts[contact] = first_name + " " + last_name
        save_phonebook()
        print(f"\n Контакт {first_name} {last_name} изменен.")
    else:
        print("\n Нет записей")
 
 # Сохранение телефонной книги
def save_phonebook():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

# Поиск контакта
def find_contact():
    print("\n")
    contact = input("Номер - ") 
    if contact in contacts:
        print(f"\n {contact}: {contacts[contact]}")
    else:
        print("\n Нет записей")
# Удаление контакта
def delete_contact():
    print("\n")
    contact = input("Номер - ") 
    if contact in contacts:
        del contacts[contact]
        save_phonebook()
        print("\n Контакт удален.")
    else:
        print("\n Нет записей")
        
# Открытие телефонной книги
def open_phonebook():
    try:
        with open("contacts.json") as file:
            global contacts
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}



open_phonebook()
phone_book()