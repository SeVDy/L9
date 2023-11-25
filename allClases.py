import random

# *********************************************************************************************************************
class Card:
    # Автоматическое действие  при создании новой карты
    def __init__(self):

        # Генерируем карточку без пробелов
        self._cardInfo = []
        for i in range(3): # Строки карточки
            self._cardInfo.append([])
            for j in range(9): # Столбцы карточки
                self._cardInfo[i].append(j)
                value = 0
                while value ==0 or y: # проверяем значение на уникальность в карте
                    value = random.randint(1 if j == 0 else j * 10 + 1, j * 10 + 10)
                    y = any(value in x for x in self._cardInfo)
                self._cardInfo[i][j] = value

        # Делаем 4 пробелa в каждой строке карты
        for i in range(3):
            numSpaceInRaw = 0
            for j in range(9):
                if numSpaceInRaw != 4:
                    if 9 - j > 4-numSpaceInRaw:
                        if random.randint(0,1) == 1:
                            self._cardInfo[i][j] = '  '
                            numSpaceInRaw += 1
                    else:
                        self._cardInfo[i][j] = '  '

    # метод получения информации о карте
    @property
    def getCardInfo(self):
        return self._cardInfo

    # метод модификации карточки
    def modifyCard(self, num):
        inRange = False
        for i in range(3):
            if num in self._cardInfo[i]:
                x = self._cardInfo[i].index(num)
                self._cardInfo[i][x] = '--'
                inRange = True
        return inRange

    # метод печать карточки
    def printCard(self,Player):
        lenSymb = '-' *int((26 - len(Player))/2)
        firstRaw = lenSymb +Player +lenSymb
        print('\n' + firstRaw)
        for raw in self._cardInfo:
                print(' '.join(map(str, raw)))
        print('-' * 26)
        return firstRaw
# *********************************************************************************************************************
class Generator:
    def __init__(self):
        self.poolList = [i for i in range( 1, 91)]

    def mixBag(self):
        x =0
        while x not in self.poolList or self.poolList == []:
            x = random.randint(1, 91)
        self.poolList.remove(x)
        return x
# *********************************************************************************************************************
class Player:
    def __init__(self):
       pass

    def win(self, playerCard):
        complCard = False
        count = 0
        for i in range(3):
            for j in playerCard[i]:
                count += 1
                if isinstance(j,int):
                    break
        # Если во всей карточке тип str, игрок победил
        if count == 27:
            complCard = True
        return complCard

    def getAnswer(self, tub, card):
        try:
            answPlayer = input()
            if 'да' != answPlayer != 'нет':
                raise ValueError
        except ValueError:
            print('Неверный ответ!')
            answPlayer = ''
        return answPlayer
#.......................................................................................................................
class NPC(Player):
    def __init__(self):
        pass
    def getAnswer(self, tub, card):
        answNPC = 'нет'
        for i in range(3):
            if tub in card[i]:
                answNPC = 'да'
        print(answNPC)
        return answNPC



