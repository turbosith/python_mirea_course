class Move:
    def __init__(self, text, next_location_mark):
        self.text = text
        self.next_location_mark = next_location_mark


class Location:
    def __init__(self, name=None, mark=None, description=None, next_movements=None):
        self.name = name
        self.mark = mark
        self.description = description
        self.next_movements = next_movements


class TextGame:
    def __init__(self):
        self.locations = {}
        self.start_location = None
        self.end_locations = list()

    def add_location(self, new_location):
        self.locations[new_location.mark] = new_location

    def set_start_location(self, start_location):
        self.locations[start_location.mark] = start_location
        self.start_location = start_location

    def add_end_location(self, end_location):
        self.locations[end_location.mark] = end_location
        self.end_locations.append(end_location.mark)

    def start_game(self):
        current_location = self.start_location
        while current_location.mark not in self.end_locations:
            print()
            print(current_location.name + "\n")
            print(current_location.description)
            for i in range(1, len(current_location.next_movements) + 1):
                print(i, ') ' + current_location.next_movements.get(i).text)
            location_decision = int(input())

            current_location = self.locations.get(
                current_location.next_movements.get(location_decision).next_location_mark)

        print(current_location.description)


location1 = Location("Начало игры",
                     1,
                     "Вы в лесу, идёт дождь. Нужно найти, где укрыться от дождя",
                     {1: Move("Пойти на запад.", 2)})

location2 = Location("Локация №2",
                     2,
                     "Вы вышли на поляну. Деревья не урывают вас от дождя, нужно уйти отсюда, иначе вы промокните.",
                     {1: Move("Проход на запад.", 3),
                      2: Move("Проход на восток.", 1),
                      3: Move("Проход на юг.", 4)
                      })

location3 = Location("Локация №3",
                     3,
                     "Ааа, впереди яма. Придётся вернуться назад.",
                     {1: Move("Проход на восток", 2),
                      2: Move("Проход на запад", 5)
                      })
location4 = Location("Локация №4",
                     4,
                     "Вы пришли к горе. Вдали веднеются огни деревни. Вы двигаетесь в правильном направлении!",
                     {1: Move("Проход на север", 2),
                      2: Move("Проход на юг", 6)
                      })

location5 = Location(description="Вы упали в яму и умерли! Конец игры!", mark=5)

location6 = Location("Локация №6",
                     6,
                     "Вы вышли к болоту. Придется его преодолеть.",
                     {1: Move("Проход на север", 4),
                      2: Move("Проход на восток", 7)
                      })
location7 = Location("Локация №7",
                     7,
                     "Перед вами камень с надписью:" + "\n" +
                     "На север пойдешь: коня потеряешь." + "\n" +
                     "На запад пойдешь: болото найдешь. " + "\n" +
                     "На юг пойдешь: укрытие от дождя найдешь." + "\n" +
                     "На восток пойдешь: смерь найдешь.",
                     {1: Move("Проход на север", 8),
                      2: Move("Проход на юг", 9),
                      3: Move("Проход на восток", 10),
                      4: Move("Проход на запад", 6),
                      })
location8 = Location("Локация №8",
                     8,
                     "У вас не было коня... Вы ничего не потеряли, но попали в тупик.",
                     {1: Move("Проход на юг", 7),
                      })
location9 = Location(description="Вы нашли ночлег! Победа!", mark=9)
location10 = Location(description="Вы нашли смерть! Поражение!", mark=10)
game = TextGame()
game.set_start_location(location1)
game.add_location(location2)
game.add_location(location3)
game.add_location(location4)
game.add_location(location6)
game.add_location(location7)
game.add_location(location8)
game.add_end_location(location9)
game.add_end_location(location10)
game.add_end_location(location5)
game.start_game()
