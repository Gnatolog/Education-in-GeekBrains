# Модуль содержащий основные функции программы
import text

telephone_numbers = {}


def open_file():
    """Функция открывает файл и передаё все данные в словарь списков для дальнейшой работы"""

    with open('telephone_directory.txt', 'r', encoding="utf-8") as fs:
        file = fs.readlines()
        if len(file) == 0:
            print(text.empty_directory)
        else:
            for i in file:
                if i:
                    contact = i.strip().split(':')
                    telephone_numbers[contact[0]] = [contact[1], contact[2], contact[3]]
            print(f"\t\n{text.open_file}\n".upper())

    return telephone_numbers


def show_contacts():
    """функция показывает все контакты"""
    if len(telephone_numbers) == 0:
        print(text.empty_directory)
    else:
        print(f"\t\n{text.directory.upper()}\n")
        for val in telephone_numbers.values():
            print(f"{text.tabl[0]}: {val[0]}\n"
                  f"{text.tabl[1]}: {val[1]}\n"
                  f"{text.tabl[2]}: {val[2]}\n")


def save_contact():
    """функция сохраняет изменения в телефонный справочник"""
    with open('telephone_directory.txt', 'w', encoding='utf-8') as fs:
        for key, val in telephone_numbers.items():
            fs.write(f"{key}:{val[0]}:{val[1]}:{val[2]}\n")
        print(f"{text.save}")


def exit_s():
    """Функция выходит из справочника"""
    print(text.exit_s.upper())


def add_contact(data):
    """Добавление контакта"""
    id_contact = 1
    if len(telephone_numbers) == 0:
        telephone_numbers[id_contact] = data
        print(text.text_add_cotacs)
    else:
        for i in telephone_numbers.keys():
            id_contact = int(i) + 1
        telephone_numbers[id_contact] = data
        print(text.text_add_cotacs)


def find_contact(data):
    """Функция ищет контакты в телефоном справочнике"""
    contacts = []
    for val in telephone_numbers.values():
        for i in data:
            if i is None:
                continue
            else:
                if i.lower() in val[0].lower():
                    contacts.append(val)
    return contacts


def change_contact(new_data, change_data):
    """Фукнция меняет данные у контакта"""

    flag = False
    count = 0
    new_datas = {}
    for i in change_data:
        if i is None:
            continue
        else:
            if i != 'None':
                change_data = i

    for i in new_data:
        count += 1
        if i is None:
            continue
        else:
            if i != 'None':
                new_datas[count] = i

    for i in new_datas.keys():
        new_data = i

    for val in telephone_numbers.values():
        print(change_data)
        print(type(change_data))
        if change_data.lower() in val[0].lower():
            if new_data == 1:
                val[0] = new_datas[new_data]
            if new_data == 2:
                val[1] = new_datas[new_data]
            if new_data == 3:
                val[2] = new_datas[new_data]
                flag = True
        elif change_data.lower() in val[1].lower():
            if new_data == 1:
                val[0] = new_datas[new_data]
            if new_data == 2:
                val[1] = new_datas[new_data]
            if new_data == 3:
                val[2] = new_datas[new_data]
                flag = True
        elif change_data.lower() in val[2].lower():
            if new_data == 1:
                val[0] = new_datas[new_data]
            if new_data == 2:
                val[1] = new_datas[new_data]
            if new_data == 3:
                val[2] = new_datas[new_data]
            flag = True

    return flag


def delete_contact(delet_data):
    """Функция удаляет контакт"""
    flag = False
    for i in delet_data:
        if i is None:
            continue
        else:
            if i != "None":
                delet_data = i
    delete = None
    print(delet_data)
    for key, val in telephone_numbers.items():
        if delet_data in val[0]:
            delete = key
            flag = True
        if delet_data in val[1]:
            delete = key
            flag = True
        if delet_data in val[2]:
            delete = key
            flag = True
    telephone_numbers.pop(delete)
    return flag

def answer_exit(answer:str):
    if answer.lower() == 'y':
        save_contact()
