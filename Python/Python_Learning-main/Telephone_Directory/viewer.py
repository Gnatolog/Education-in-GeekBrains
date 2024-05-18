# Модуль визуализации данных программы
import text


def Show_menu():
    """функция выводит  главное меню"""
    for i, items in enumerate(text.main_menu):
        if i == 0:
            print(f"{items}:")
        else:
            print(f"\t{i} {items}")

    select_options = input(f'{text.requests}{text.zero}{len(text.main_menu) - 1}: ')
    while True:
        if select_options.isdigit() and 0 < int(select_options) < len(text.main_menu):
            return int(select_options)
        else:
            select_options = input(f"{text.main_menu_erro}{text.zero}{len(text.main_menu) - 1}: ")


def add_data_contact():
    """функция запрашивает у пользователя данные"""

    name = input("Введите ФИО: ")
    if name:
        name = name
    else:
        name = None

    tel_numbers = input("Введите номер телефона: ")
    if tel_numbers:
        tel_numbers = tel_numbers
    else:
        tel_numbers = None

    comments = input("Введите коментарии: ")
    if comments:
        comments = comments
    else:
        comments = None

    return name, tel_numbers, comments


def show_contact(contacts: list) -> print:
    """ Функци выводит результат поиска контакта"""
    if contacts:
        print(text.contct_find)
        for i in contacts:
            print(f"\t\n{i[0]} {i[1]} {i[2]}\n")
    else:
        print(text.contact_not_find)


def contact_change(flag: bool) -> print:
    """Функция выводит результат работы поиска контака"""
    if flag:
        print(text.contact_change)
    else:
        print(text.contact_not_find)


def help_s():
    print(text.what_change)


def contact_delete(flag: bool) -> print:
    """Функция выводит результат удаления контакта"""
    if flag:
        print(text.delet_contact)
    else:
        print(text.contact_not_find)


def save_toexits() -> str:
    """Функция зарпашивает у пользователя разрешение на сохранения файла"""

    print(text.save_toexit)
    answer = input("Если хотите сохранить нажмите 'y': ")
    return answer
