from robot import Robot


class RobotManager:
    @staticmethod
    def count_robots(robots):
        count = 0
        if not isinstance(robots, (list, tuple)):
            return -1

        for robot in robots:
            if isinstance(robot, Robot):
                count += 1

        return count

    @staticmethod
    def count_total_price(robots):

        total_price = 0
        for robot in robots:
            if isinstance(robot, Robot):
                total_price = total_price + robot._price

        return total_price