from robot import Robot
from convertor import DataConvertor
from manager import RobotManager
from creator import RobotCreator


def main():
    ls = RobotCreator.create(5)
    print(DataConvertor.convert_to_string(ls))

    calc_total_price = RobotManager.count_total_price(ls)
    count_robots = RobotManager.count_robots(ls)

    print(f"Total count: {calc_total_price}$"
          f"\nCount of robots: {count_robots}")


if __name__ == "__main__":
    main()