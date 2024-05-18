import text


def show_start():
    for i, val in enumerate(text.start_fight):
        if i == 0:
            print(val)
        else:
            print(f"{i}-{val}".upper())
    select_option = input()
    while True:
        if select_option.isdigit() and 0 < int(select_option) < len(text.start_fight):
            return int(select_option)
        else:
            select_option = input("Вы ввели некоректные данные введдите 1 или 2")


def continuation():
    """Фунция отображения меню во время боя"""
    for i, val in enumerate(text.start_fight):
        if i != 0:
            print(f"{i}-{val}".upper())
    select_option = input()
    while True:
        if select_option.isdigit() and 0 < int(select_option) < len(text.start_fight):
            return int(select_option)
        else:
            select_option = input("Вы ввели некоректные данные введдите 1 или 2")


def name_figter():
    """Функция для назначенмя имени бойца"""

    name = input(text.name)
    return name


def game_over(health_1, health_2):
    """Фунуция заверщения игры"""

    if health_1 <= 0 or health_2 <= 0:
        print(text.text_game_over)
        return 0


# удар по сопернику
def status_fighter(fighter):
    """Функция показывает статус бойца"""

    if fighter.health < 0:
        fighter.health = 0
        print(f"{fighter.name} {text.tex_hp}: {fighter.health}\n")
    else:
        print(f"{fighter.name} {text.tex_hp}: {fighter.health}\n")


def winer(fighter):
    return print(f"\t\n{text.wine}: {fighter.name}")
