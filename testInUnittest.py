import unittest

from allClases import Card, Generator, Player, NPC

class UTestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card()

    def tearDown(self):
        pass

    def testInit(self):
        mask = "[[][][]]"
        func = lambda x: str(x).translate(str.maketrans('', '', " ',0123456789-"))
        self.assertEqual(func(self.card.getCardInfo), mask,
                         'Неправильная структура!')
        for i in range(3):
            numInt = 0
            numStr = 0
            for j in range(9):
                if self.card.getCardInfo[i][j] == '  ':
                    numStr += 1
                if isinstance(self.card.getCardInfo[i][j], int):
                    numInt += 1
            self.assertTrue(numStr == 4 and numInt == 5,
                            f'Некорректно заполняется строка карты №{j}!')
            self.assertEqual(len(set(self.card.getCardInfo[i])), 6,
                             f'В строке №{i} есть дубликаты!')

    def testModifyCard(self):
        flag = False
        for i in range(1, 91):
            self.card.modifyCard(i)
            for j in range(3):
                if '--' in self.card.getCardInfo[j]:
                    flag = True
                    break
        self.assertTrue(flag,
                        'Не модифицируется карта!')

    def testPrintCard(self):
        self.assertEqual(self.card.printCard('Игрок'),'-' * 10 + 'Игрок' + '-' * 10,
                         'Некорректно создается верхняя строка!' )

class TestGenerator(unittest.TestCase):
    def setUp(self):
        self._x = [x for x in range(1, 91)]
        self.generator = Generator()
    def tearDown(self):
        pass

    def testInit(self):
        self.assertEqual(self.generator.poolList, self._x,
                         'Некорректно создается список с бочонками!')

    def testMixBag(self):
        tempList = []
        for i in range(1,91):
            tempList.append(self.generator.mixBag())
        self.assertTrue(len(self.generator.poolList) == 0 and sorted(tempList) == self._x,
                        'Некорректно удаляются данные из пула!')

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.maskWin = [[], [], []]
        for i in range(3):
            for j in range(4):
                self.maskWin[i].append('  ')
            for k in range(5):
                self.maskWin[i].append('--')
    def tearDown(self):
        pass

    def testWin(self):
       self.assertTrue(self.player.win(self.maskWin),
                       'Неверно определяется признак победителя!')


class TestNPC(unittest.TestCase):
    def setUp(self):
        self.NPC = NPC()
        self.card = Card()
        self.num = 10
    def tearDown(self):
        pass

    def testGetAnswer(self):
        answMask = 'нет'
        x = self.NPC.getAnswer(self.num, self.card.getCardInfo)
        for i in range(3):
            for j in self.card.getCardInfo[i]:
                if j == self.num:
                    answMask = 'да'
                    break
        self.assertTrue(x == answMask,
                        'Неверный ответы от NPC')
