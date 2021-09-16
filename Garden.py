import random


class Tomato:

    states = {1: "Зелёный", 2: "Желтый", 3: "Красный"}

    def __init__(self, first):
        self._index = first
        self._state = self.states[1]

    def info(self):
        print(self._state)

    def grow(self):
        if self._state == self.states[1]:
            self._state = self.states[2]
        else:
            self._state = self.states[3]

    def is_ripe(self):
        if self._state == self.states[3]:
            return True
        else:
            return False


class TomatoBush:

    def __init__(self, count):
        self.tomatoes = []
        for i in range(count):
            self.tomatoes.append(Tomato(i))

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        check = False
        for tomato in self.tomatoes:
            check = tomato.is_ripe()
        return check

    def give_away_all(self):
        for tomato in self.tomatoes:
            del tomato
        self.tomatoes.clear()


class Gardener:

    def __init__(self, name):
        self.name = name
        self._plant = Tomato(5)

    def work(self):
        self._plant.grow()

    def work_with_bush(self, obj):
        print("Ухаживаем...")
        obj.grow_all()

    def harvest(self, obj):
        print("Проверяем на зрелось...")
        if obj.all_are_ripe():
            print("Созрело!\nСобираем урожай...")
            obj.give_away_all()
        else:
            print("Куст ещё не созрел!")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:\n"
              "Вы можете стать сдовником, который ухаживает за кустом с помидорами.\n"
              "Собирайте выращивайте, проверяйте на зрелось и собирайте урожай.")


#1
Gardener.knowledge_base()
#2
bush = TomatoBush(random.randint(1, 5))
gardener = Gardener(input("\nВведите своё имя: "))
#3
gardener.work_with_bush(bush)
#4 and 5
gardener.harvest(bush)
while True:
    if not bush.all_are_ripe():
        gardener.work_with_bush(bush)
    else:
        break
#6
gardener.harvest(bush)

