class Phone_directory():
    """Класс телефонный справочник"""

    def __init__(self, firstname='', lastname=None, lastname2=None, tel=None, newname=None,
                 new_tel=None, comments=None):
        self.firstname = firstname
        self.lastname = lastname
        self.newname = newname
        self.new_tel = new_tel
        self.lastname2 = lastname2
        self.comments = comments
        self.tel = tel
        self.phone_numbers = {}

    def add_number(self):
        """Фукция добовляет контакты в справочник"""

        self.phone_numbers
        with open('telephone_directory.txt', 'r', encoding='utf-8') as fh:
            for i in fh.readlines():
                if i:
                    key, val = i.strip().split(':')
                    self.phone_numbers[key] = val
        if self.phone_numbers:
            for i in self.phone_numbers.keys():
                i = str(i)
                i = i.strip().split()
                if i[0] == self.firstname:
                    return "Такой контакт уже существует"
        else:
            self.phone_numbers[self.firstname] = self.tel
        with open('telephone_directory.txt', 'a', encoding='utf-8') as fh:
            fh.write('{} {}:{} {}\n'.format(self.firstname, self.lastname, self.tel,
                                            self.comments))
        return "Контакт успешно записан"

    def delet_contact(self):

        """Функция удаляет контакты из справочника"""

        self.phone_numbers
        word = []
        count = 0
        with open('telephone_directory.txt', 'r', encoding='utf-8') as fh:
            for i in fh.readlines():
                count += 1
                if i:
                    key = i.strip().split()
                    if key[0] != self.firstname:
                        word.append(key[0])
                        key, val = i.strip().split(':')
                        self.phone_numbers[key] = val
            if count == len(word):
                return "Контакт не существует"
        with open('telephone_directory.txt', 'w', encoding='utf-8') as fh:
            for key, val in self.phone_numbers.items():
                fh.write(f'{key}:{val}\n')
            return "Контакт успешно удалён"

    def find_contact(self):

        """Функция ищет контакты в справочнике"""

        self.phone_numbers
        with open("telephone_directory.txt", 'r', encoding='utf-8') as fh:
            for i in fh.readlines():
                if i:
                    key = i.strip().split()
                    if key[0] == self.firstname:
                        key, val = i.strip().split(':')
                        self.phone_numbers[key] = val
                        return f"{key} - {self.phone_numbers[key]}"

            return "Контакт не найден"

    def show_contact(self):

        """Функция показывает все контакты из справочника"""

        with open("telephone_directory.txt", 'r', encoding='utf-8') as fh:
            for i in fh.readlines():
                if i:
                    key, val = i.strip().split(':')
                    self.phone_numbers[key] = val
            return self.phone_numbers.items()

    def update_contacts(self):

        """Функция обновляет контакты в справочнике"""
        # при добавление контактв меняет и его без добавлния контакта меняет только пользователя
        change_val = ''
        with open("telephone_directory.txt", 'r', encoding='utf-8') as fh:
            for i in fh.readlines():
                if i:
                    key = i.strip().split()
                    if key[0] == self.firstname:
                        print(key[0])
                        if self.new_tel:
                            change_val = self.new_tel
                        else:
                            key, val = i.strip().split(":")
                            change_val = val
                    else:
                        key, val = i.strip().split(':')
                        self.phone_numbers[key] = val
                        self.phone_numbers[self.newname] = change_val

        with open("telephone_directory.txt", 'w', encoding='utf-8') as fh:
            if len(self.phone_numbers) == 0:
                fh.write('{} {}:{} {}\n'.format(self.newname, self.lastname, change_val,
                                                self.comments))
                return "Изменения внесены"

            for key, val in self.phone_numbers.items():
                if key == self.newname:
                    fh.write('{} {}:{} {}\n'.format(self.newname, self.lastname, change_val,
                                                    self.comments))
                else:
                    fh.write('{} : {}\n'.format(key, val))
            return "Изменения внесены"

    def create_telephone_directory(self):
        with open('telephone_directory.txt', 'w', encoding='utf-8') as fh:
            fh.write('{} : {}\n'.format("hello", "world"))
            return "Справочник создан"


# Управляющий модуль


flag = True
while flag:
    print('''
    0 - создать справочник (рекомендовано при первом запуске)
    1 - добавить контакт
    2 - удалить контакт
    3 - найти контакт
    4 - показать контакты
    5 - обновить контакт
    6 - выйти''')
    answer = input("\nЧто вы хотите сделать введите 1,2,3, или 6 если хотите выйти: ")

    if answer == '0':
        telefon = Phone_directory()
        print(telefon.create_telephone_directory())
    if answer == '1':
        insert_name = (input("Enter name contact: ")).lower()
        inset_lastname = (input("Enter lastname: ")).lower()
        insert_number = input("Ennter number contact: ")
        insert_comments = (input("Enter comment: ")).lower()
        telefon = Phone_directory(firstname=insert_name, tel=insert_number,
                                  lastname=inset_lastname, comments=insert_comments)
        print(telefon.add_number())
    if answer == '2':
        insert_name = (input("Enter name contact: ")).lower()
        telefon = Phone_directory(firstname=insert_name, )
        print(telefon.delet_contact())
    if answer == '3':
        insert_name = (input("Enter name contact: ")).lower()
        telefon = Phone_directory(firstname=insert_name, )
        print(telefon.find_contact())
    if answer == '4':
        telefon = Phone_directory()
        print(*telefon.show_contact())
    if answer == '5':
        insert_name = (input("Enter name contact: ")).lower()
        insert_newname = (input("Enter newname contact: ")).lower()
        insert_lastname = (input("Enter lastname: ")).lower()
        insert_number = input("Enter new number: ")
        insert_comments = (input("Enter comment: ")).lower()
        telefon = Phone_directory(firstname=insert_name, newname=insert_newname,
                                  new_tel=insert_number, lastname=insert_lastname,
                                  comments=insert_comments)
        print(*telefon.update_contacts())
    if answer == '6':
        flag = False

print('GoodBye'.upper())

