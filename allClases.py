import random


# *********************************************************************************************************************


class Card:
    # Автоматическое действие  при создании новой карты
    def __init__(self):

        # Генерируем карточку без пробелов
        self._cardInfo = []
        for i in range(3):  # Строки карточки
            self._cardInfo.append([])
            for j in range(9):  # Столбцы карточки
                self._cardInfo[i].append(j)
                value = 0
                while value == 0 or y:  # проверяем значение на уникальность в карте
                    value = random.randint(1 if j == 0 else j * 10 + 1, j * 10 + 10)
                    y = any(value in x for x in self._cardInfo)
                self._cardInfo[i][j] = value

        # Делаем 4 пробелa в каждой строке карты
        for i in range(3):
            num_space_in_raw = 0
            for j in range(9):
                if num_space_in_raw != 4:
                    if 9 - j > 4 - num_space_in_raw:
                        if random.randint(0, 1) == 1:
                            self._cardInfo[i][j] = '  '
                            num_space_in_raw += 1
                    else:
                        self._cardInfo[i][j] = '  '

    # метод получения информации о карте
    @property
    def getCardInfo(self):
        return self._cardInfo

    # метод модификации карточки
    def modifyCard(self, num):
        in_range = False
        for i in range(3):
            if num in self._cardInfo[i]:
                x = self._cardInfo[i].index(num)
                self._cardInfo[i][x] = '--'
                in_range = True
        return in_range

    # метод печать карточки
    def printCard(self, player):
        len_symb = '-' * int((26 - len(player)) / 2)
        first_raw = len_symb + player + len_symb
        print('\n' + first_raw)
        for raw in self._cardInfo:
            print(' '.join(map(str, raw)))
        print('-' * 26)
        return first_raw


# *********************************************************************************************************************


class Generator:
    def __init__(self):
        self.poolList = [i for i in range(1, 91)]

    def mixBag(self):
        x = 0
        while x not in self.poolList or self.poolList == []:
            x = random.randint(1, 91)
        self.poolList.remove(x)
        return x


# *********************************************************************************************************************


class Player:

    @staticmethod
    def win(player_card):
        compl_card = False
        count = 0
        for i in range(3):
            for j in player_card[i]:
                count += 1
                if isinstance(j, int):
                    break
        # Если во всей карточке тип str, игрок победил
        if count == 27:
            compl_card = True
        return compl_card

    def getAnswer(self, tub, card):
        try:
            answ_player = input()
            if 'да' != answ_player != 'нет':
                raise ValueError
        except ValueError:
            print('Неверный ответ!')
            answ_player = ''
        return answ_player


# .......................................................................................................................


class NPC(Player):
    def getAnswer(self, tub, card):
        answ_npc = 'нет'
        for i in range(3):
            if tub in card[i]:
                answ_npc = 'да'
        print(answ_npc)
        return answ_npc
