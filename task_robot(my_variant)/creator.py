import random
import string
from robot import Robot


class RobotCreator:

    @staticmethod
    def create(size):
        NAMES = ("Optimus Prime", "Alfa Trion", "Arsy", "Bamblby", "Blayd", "Slag",
                 "Fixit", "Swoom", "Cheize", "Fallback","Robocop", "Sunny")  # tuple

        ALFABET = string.ascii_uppercase

        MAX_INTELLEGENCE = 100
        MIN_INTELLEGENCE = 1

        MAX_PRICE = 1_000_000_000
        MIN_PRICE = 1_000_000

        ls = []

        for _ in range(size):
            name = random.choice(NAMES)  # метод choice
            model = ALFABET[random.randrange(len(ALFABET))]
            intellegence_level = random.randint(MIN_INTELLEGENCE, MAX_INTELLEGENCE)
            price = random.randint(MIN_PRICE, MAX_PRICE)

            robot = Robot(name, model, intellegence_level, price)

            ls.append(robot)

        return ls
