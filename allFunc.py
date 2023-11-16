def menu(choose):
    while choose not in range(1,3):
        print('\nДобро пожаловать в лототрон 2023')
        print('1. Новая игра')
        print('2. Выход')
        try:
            choose = int(input('\nВыберите пункт: '))
        except ValueError:
            print('Пункт выбран не верно!')
        if choose not in range(1,3):
            print('Пункт выбран некорректно!')
    return choose

def numPlayers():
    while True:
        try:
            numPlayer = int(input('Укажите количество игроков: '))
            if numPlayer == 0:
                print('Количество игроков указано не верно!')
                continue
            return numPlayer
            break
        except ValueError:
            print('Количество игроков указано не верно!')

def mode():
    while True:
        print('Режимы игры:')
        print('1. Игрок - Игрок')
        print('2. Игрок - Компьютер')
        print('3. Компьютер - Компьютер')
        try:
            mode = int(input('\nВыберите режим игры: '))
            if mode not in range(1,4):
                print('Режим указан не верно!')
                continue
            return mode
            break
        except ValueError:
            print('Режим указан не верно!')

