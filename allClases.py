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
                y = False
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

    def __str__(self):
        print('-' * 26)
        for raw in self._cardInfo:
            print(' '.join(map(str, raw)))
        print('-' * 26)
        return ''

    def __eq__(self, other):
        if isinstance(self._cardInfo, list) == isinstance(self._cardInfo, list):
            count = 0
            for i in range(3):
                for j in range(9):
                    if self.getCardInfo[i] == other.getCardInfo[i]:
                        count += 1
            return count == 27
        else:
            return False

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
        self.numTub = 0

    def __int__(self):
        return self.numTub

    def __str__(self):
        return str(self.numTub)

    def __eq__(self, other):
        return self.poolList == other.poolList and self.numTub == other.numTub

    def __len__(self):
        return len(self.poolList)

    def mixBag(self):
        while self.numTub not in self.poolList or self.poolList == []:
            self.numTub = random.randint(1, 91)
        self.poolList.remove(self.numTub)
        return self.numTub


# *********************************************************************************************************************


class Player:
    def __init__(self):
        self._typePlayer = 'Player'

    def __str__(self):
        return self._typePlayer

    def __eq__(self, other):
        return self.getTypePlayer == other.getTypePlayer

    def getTypePlayer(self):
        return self._typePlayer

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
    def __init__(self):
        super().__init__()
        self._typePlayer = 'NPC'

    def __str__(self):
        return self._typePlayer

    def getAnswer(self, tub, card):
        answ_npc = 'нет'
        for i in range(3):
            if tub in card[i]:
                answ_npc = 'да'
        print(answ_npc)
        return answ_npc
