# Функции проверяем через Pytest

from allClases import Card, Generator, Player, NPC

if __name__ == '__main__':
    pass


class TestCard:
    def setup(self):
        self.card = Card()

    def teardown(self):
        pass

    def test_init(self):
        mask = "[[][][]]"
        func = lambda x: str(x).translate(str.maketrans('', '', " ',0123456789-"))
        assert func(self.card.getCardInfo) == mask, 'Неправильная структура!'
        j = 0
        for i in range(3):
            num_int = 0
            num_str = 0
            for j in range(9):
                if self.card.getCardInfo[i][j] == '  ':
                    num_str += 1
                if isinstance(self.card.getCardInfo[i][j], int):
                    num_int += 1
            assert num_str == 4 and num_int == 5, f'Некорректно заполняется строка карты №{j}!'
            assert len(set(self.card.getCardInfo[i])) == 6, f'В строке №{i} есть дубликаты!'

    def test_modify_card(self):
        flag = False
        for i in range(1, 91):
            self.card.modifyCard(i)
            for j in range(3):
                if '--' in self.card.getCardInfo[j]:
                    flag = True
                    break
        assert flag, 'Не модифицируется карта!'

    def test_print_card(self):
        assert self.card.printCard('Игрок') == '-' * 10 + 'Игрок' + '-' * 10, 'Некорректно создается верхняя строка!'


class TestGenerator:
    def setup(self):
        self._x = [x for x in range(1, 91)]
        self.generator = Generator()

    def teardown(self):
        pass

    def test_init(self):
        assert self.generator.poolList == self._x, 'Некорректно создается список с бочонками!'

    def test_mix_bag(self):
        temp_list = []
        for i in range(1, 91):
            temp_list.append(self.generator.mixBag())
        assert len(self.generator.poolList) == 0 and sorted(temp_list) == self._x, \
            'Некорректно удаляются данные из пула!'


class TestPlayer:
    def setup(self):
        self.player = Player()
        self.maskWin = [[], [], []]
        for i in range(3):
            for j in range(4):
                self.maskWin[i].append('  ')
            for k in range(5):
                self.maskWin[i].append('--')

    def test_win(self):
        assert self.player.win(self.maskWin), 'Неверно определяется признак победителя!'


class TestNPC:
    def setup(self):
        self.NPC = NPC()
        self.card = Card()
        self.num = 10

    def teardown(self):
        pass

    def test_get_answer(self):
        answ_mask = 'нет'
        x = self.NPC.getAnswer(self.num, self.card.getCardInfo)
        for i in range(3):
            for j in self.card.getCardInfo[i]:
                if j == self.num:
                    answ_mask = 'да'
                    break
        assert x == answ_mask, 'Неверный ответы от NPC'
