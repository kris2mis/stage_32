# Необходимо описать класс Robot, на базе которого можно будет создавать эк-
# земпляры роботов. У объекта-робота должны быть минимум следующие пара-
# метры: название (name) или модель (model), уровень интеллекта (intelligence
# level) по шкале от 0 до 100 и стоимость ( price). Дополнительные параметры ро-
# бота можно придумать самостоятельно исходя из расширения предметной об-
# ласти. Также робот должен обладать следующим поведением:
#  во время создания робота, на экран должна выводится надпись «Робот
# 'название_робота' был создан.» («Robot 'name' was created.»);
#  во время уничтожения робота, на экран должна выводится надпись «Ро-
# бот 'название_робота' был уничтожен.» («Robot 'name' was destroyed.»);
#  метод для приветствия say_hello(name=””), который должен возвращать
# следующее сообщение: «Робот 'название_робота' приветствует тебя,
# особь человеческого рода.» («Robot 'name' greets you, individual of the human
# race.»);
#  метод __str__(…) для представления состояния объекта в виде строки;
#  соответствующие свойства для инкапсуляции своей внутренней реализа-
# ции и защиты данных от противоречивого использования (цена робота не
# должна быть отрицательной, а его интеллект должен быть в пределах диа-
# пазона от 0 до 100).
# Далее требуется написать небольшую программу, которая бы создавала пару ро-
# ботов с различными параметрами и определяла общую стоимость всех роботов,
# а также находила самых интеллектуальных роботов (да, уровень интеллекта у
# различных роботов может быть одинаковым). Подсказка: данный функционал
# можно описать в виде статических методов класса RobotManager, который бы
# отвечал за бизнес-логику программной системы, а также дополнительных сер-
# висных классов: RoborCreator (служит для создания списка объектов-роботов) и
# DataConvertor (для преобразования списка роботов в строку для удобства вы-
# вода результирующих данных).
# Дополнительно в программе должна вестись статистика: сколько всего роботов
# было создано с момента старта программы, сколько было уничтожено и сколько
# в данный момент находится в эксплуатации. Подсказка: используйте соответству-
# ющие поля самого класса Robot, его свойства и методы.


class Robot:
    def __init__(self, name, model, intelligence_level, price):
        self._name = name
        self._model = model
        self._intelligence_level = intelligence_level
        self._price = price


    def say_hello(self):
        str = f"Robot {self._name} greets you, individual of the human race."
        return str

    def __str__(self):
        return (f"Robot {self._name}-{self._model} was created: "
                f"intelligence level = {self._intelligence_level}, "
                f"price = {self._price}$.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    @property
    def intelligence_level(self):
        return self._intelligence_level

    @intelligence_level.setter
    def intelligence_level(self, intelligence_level):
        if self._intelligence_level > 0 and self._intelligence_level <= 100:
            self._intelligence_level = intelligence_level

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if self._price > 0:
            self._price = price
