import random


class Fighter:
    """Класс бойца"""
    def __init__(self, name='Shawkan'):
        self.name = name
        self.health = 100

    def punch(self, fighter):
        """Метод удара"""
        punches = random.randint(1, 21)
        fighter.health = fighter.health - punches
        return fighter.health

    def block(self, fighter):
        """Метод блока"""
        punches = random.randint(1, 10)
        fighter.health = fighter.health - (punches // 2)
        return fighter.health

    def intelect(self, fighter_1, fighter_2):
        """Метод искуственного интелекта"""

        fighter_1.health = fighter_2.punch(fighter_1)  # ответный удар соверника

        if fighter_2.health <= 25:
            choice = random.randint(1, 2)

            if choice == 1:
                fighter_1.health = fighter_2.punch(fighter_1)

            else:
                fighter_2.health = fighter_1.block(fighter_2)

        if fighter_2.health <= 10:
            fighter_2.health = fighter_1.block(fighter_2)

