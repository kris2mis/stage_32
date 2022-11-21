# Необходимо создать небольшую программу-менеджер для ведения статистики
# за футбольными игроками. Для чего необходимо спроектировать класс буду-
# щих футбольных игроков со следующими характеристиками: имя (name), фами-
# лия (surname), количество забиты голов (goal) – минимум один гол, количество
# отданных голевых передач (assist) – минимум одна голевая передача. Можно
# также добавить другие параметры исходя из самостоятельного расширения те-
# кущей предметной области. Класс также должен содержать свойства, которые
# бы позволили изменить состояние объекта, а также инициализатор для перво-
# начальной инициализации объекта и метод __str__() для преобразования состо-
# яния объекта в строковый тип данных.
# Реализовать небольшую логику, которая бы определяла, кто из игроков достоин
# получить золотой мяч. В качестве критериев оценивания можно выбрать сле-
# дующие: или по максимальным забиты голам (в случае, если количество заби-
# тых голов одинаково – тогда по голевым передачам), или вместе учитывать по
# голевым передачам и забитым голам по формуле: 3 * goal + assist = result (если
# результат равный, то золотой мяч отдаётся тому игроку, кто больше забил голов).


class FootballPlayer:
    def __init__(self, name, surname, goal=1, assist=1):
        self._name = name
        self._surname = surname
        self._goal = goal
        self._assist = assist

    def __str__(self):
        return (f"{self._name} {self._surname}: "
                f"goals = {self._goal}, "
                f"assists = {self._assist}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        self._surname = surname

    @property
    def goal(self):
        return self._goal

    @goal.setter
    def goal(self, goal):
        self._goal = goal

    @property
    def assist(self):
        return self._assist

    @assist.setter
    def assist(self, assist):
        self._assist = assist

