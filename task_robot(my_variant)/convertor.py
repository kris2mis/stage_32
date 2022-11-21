from robot import Robot


class DataConvertor:

    @staticmethod
    def convert_to_string(robots):
        s = "List of robots:"

        if not isinstance(robots, (list, tuple)):
            return "List is empty"

        for robot in robots:
            if isinstance(robot, Robot):
                s += "\n" + str(robot)

        return s