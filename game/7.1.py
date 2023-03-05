class Move:
    def __init__(self, text, next_room_mark):
        self.text = text
        self.next_room_mark = next_room_mark


class Room:
    def __init__(self, name=None, mark=None, description=None, next_movements=None):
        self.name = name
        self.mark = mark
        self.description = description
        self.next_movements = next_movements


class TextGame:
    def __init__(self):
        self.rooms = {}
        self.start_room = None
        self.end_rooms = list()

    def set_start_room(self, start_room):
        self.rooms[start_room.mark] = start_room
        self.start_room = start_room

    def add_end_room(self, end_room):
        self.rooms[end_room.mark] = end_room
        self.end_rooms.append(end_room.mark)

    def add_room(self, new_room):
        self.rooms[new_room.mark] = new_room

    def start_game(self):
        current_room = self.start_room
        while current_room.mark not in self.end_rooms:
            print()
            print(current_room.name + "\n")
            print(current_room.description)
            for i in range(1, len(current_room.next_movements) + 1):
                print(i, ') ' + current_room.next_movements.get(i).text)
            room_decision = int(input())

            current_room = self.rooms.get(current_room.next_movements.get(room_decision).next_room_mark)

        print(current_room.description)


room1 = Room("Начало игры",
             1,
             "Вы в лесу, идёт дождь. Нужно найти, где укрыться от дождя",
             {1: Move("Пойти на запад.", 2)})

room2 = Room("Локация №2",
             2,
             "Вы вышли на поляну. Деревья не урывают вас от дождя, нужно уйти отсюда, иначе вы промокните.",
             {1: Move("Проход на запад.", 3),
              2: Move("Проход на восток.", 1),
              3: Move("Проход на юг.", 4)
              })

room3 = Room("Локация №3",
             3,
             "Ааа, впереди яма. Придётся вернуться назад.",
             {1: Move("Проход на восток", 2),
              2: Move("Проход на запад", 5)
              })
room4 = Room("Локация №4",
             4,
             "Вы пришли к горе. Вдали веднеются огни деревни. Вы двигаетесь в правильном направлении!",
             {1: Move("Проход на север", 2),
              2: Move("Проход на юг", 6)
              })

room5 = Room(description="Вы упали в яму и умерли! Конец игры!", mark=5)

room6 = Room("Локация №6",
             6,
             "Вы вышли к болоту. Придется его преодолеть.",
             {1: Move("Проход на север", 4),
              2: Move("Проход на восток", 7)
              })
room7 = Room("Локация №7",
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
room8 = Room("Локация №8",
             8,
             "У вас не было коня... Вы ничего не потеряли, но попали в тупик.",
             {1: Move("Проход на юг", 7),
              })
room9 = Room(description="Вы нашли ночлег! Победа!", mark=9)
room10 = Room(description="Вы нашли смерть! Поражение!", mark=10)
game = TextGame()
game.set_start_room(room1)
game.add_room(room2)
game.add_room(room3)
game.add_room(room4)
game.add_room(room6)
game.add_room(room7)
game.add_room(room8)
game.add_end_room(room9)
game.add_end_room(room10)
game.add_end_room(room5)
game.start_game()
