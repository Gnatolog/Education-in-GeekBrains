# Модуь контролирующий работу программы
import viewer
import modul


def start():
    viewer.Show_menu()


def control_menu():
    """Функция контралируюшая работу пунктов меню"""
    user_select = viewer.Show_menu()
    while True:
        match user_select:
            case 1:
                modul.open_file()  # открывает справочик для работы с ним
                user_select = viewer.Show_menu()
            case 2:
                modul.save_contact()  # сохраняет изменения в спарвочник
                user_select = viewer.Show_menu()
            case 3:
                modul.show_contacts()
                user_select = viewer.Show_menu()
            case 4:
                modul.add_contact(viewer.add_data_contact())
                user_select = viewer.Show_menu()
            case 5:
                contacts = modul.find_contact(viewer.add_data_contact())
                viewer.show_contact(contacts)
                user_select = viewer.Show_menu()
            case 6:
                viewer.help_s()
                change = modul.change_contact(viewer.add_data_contact(), viewer.add_data_contact())
                viewer.contact_change(change)
                user_select = viewer.Show_menu()
            case 7:
                delet_s = modul.delete_contact(viewer.add_data_contact())
                viewer.contact_delete(delet_s)
                user_select = viewer.Show_menu()
            case 8:
                modul.answer_exit(viewer.save_toexits())
                return modul.exit_s()
