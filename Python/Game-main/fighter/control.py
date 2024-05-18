import viewer
import modul

fighter_name_1 = viewer.name_figter()
fighter_1 = modul.Fighter(fighter_name_1)
fighter_2 = modul.Fighter()

def control_fight():
    """Функция контроля боя"""
    user_select = viewer.show_start()

    while True:
        match user_select:
            case 1:
                fighter_2.health = fighter_1.punch(fighter_2)  # удар по сопернику
                fighter_2.intelect(fighter_1, fighter_2)  # ответ компьютера
                viewer.status_fighter(fighter_1)  # вывод статуса первого игрока
                viewer.status_fighter(fighter_2)  # вывод статуса второго игрока
                control_status = viewer.game_over(fighter_1.health, fighter_2.health)
                if control_status == 0:
                    if fighter_2.health > 0:
                        viewer.winer(fighter_2)
                        break
                    else:
                        viewer.winer(fighter_1)
                        break
                else:
                    user_select = viewer.continuation()
            case 2:
                fighter_1.health = fighter_2.block(fighter_1)  # блок
                viewer.status_fighter(fighter_1)  # вывод статуса первого игрока
                viewer.status_fighter(fighter_2)  # вывод статуса второго игрока

                control_status = viewer.game_over(fighter_1.health, fighter_2.health)

                if control_status == 0:
                    if fighter_2.health > 0:
                        viewer.winer(fighter_2)
                        break
                    else:
                        viewer.winer(fighter_1)
                        break
                else:
                    user_select = viewer.continuation()
