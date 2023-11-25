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
            num_int = 0
            num_str = 0
            for j in range(9):
                if self.card.getCardInfo[i][j] == '  ':
                    num_str += 1
                if isinstance(self.card.getCardInfo[i][j], int):
                    num_int += 1
            self.assertTrue(num_str == 4 and num_int == 5,
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
        self.assertEqual(self.card.printCard('Игрок'), '-' * 10 + 'Игрок' + '-' * 10,
                         'Некорректно создается верхняя строка!')


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
        temp_list = []
        for i in range(1, 91):
            temp_list.append(self.generator.mixBag())
        self.assertTrue(len(self.generator.poolList) == 0 and sorted(temp_list) == self._x,
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
        answ_mask = 'нет'
        x = self.NPC.getAnswer(self.num, self.card.getCardInfo)
        for i in range(3):
            for j in self.card.getCardInfo[i]:
                if j == self.num:
                    answ_mask = 'да'
                    break
        self.assertTrue(x == answ_mask,
                        'Неверный ответы от NPC')
