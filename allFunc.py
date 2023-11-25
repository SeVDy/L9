def showMenu():
    print('\nДобро пожаловать в лототрон 2023')
    print('1. Новая игра')
    print('2. Выход')


def getItemMenu():
    item = 0
    try:
        item = int(input('\nВыберите пункт: '))
        if item not in range(1, 3):
            raise ValueError
    except ValueError:
        print('Пункт меню выбран не верно!')
    return item


def numPlayers():
    numPlayer = 0
    try:
        numPlayer = int(input('Укажите количество игроков: '))
        if numPlayer <= 0:
            raise ValueError
    except ValueError:
        print('Количество игроков указано не верно!')
    return numPlayer


def showMode():
    print('Режимы игры:')
    print('1. Игрок - Игрок')
    print('2. Игрок - Компьютер')
    print('3. Компьютер - Компьютер')
    print('\n4. Назад в меню')


def getItemMode():
    mode = 0
    try:
        mode = int(input('\nВыберите режим игры: '))
        if mode not in range(1, 4):
            raise ValueError
    except ValueError:
        print('Режим указан не верно!')
    return mode
