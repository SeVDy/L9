from allClases import Card, Generator, Player, NPC
from allFunc import showMenu, getItemMenu, numPlayers, showMode, getItemMode

while True:
    numPlayer = 0
    modeGame = 0

    # Меню
    showMenu()
    userItemMenu = getItemMenu()
    match userItemMenu:
        case 1: # Выбран пункт "Новая игра"

            # Выбираем количество игроков
            numPlayer = numPlayers()

            # Выбираем режим если в игре выбрано 2 игрока
            if numPlayer == 2:
                showMode()
                modeGame = getItemMode()

        case 2: # Выбран пункт "Выход"
            break

        case _: # Возвращаемся на начало
            pass

    # Условие для начала игры
    if userItemMenu == 1 and numPlayer > 0 and modeGame in range(1,4):
        new_generator = Generator()
        playersCard = {}
        playersType = {}

        # Добавляем игроков и их карточки
        for i in range(numPlayer):
            playersCard.update({i: Card()})
            match modeGame:
                case 2: # Игрок VS NPC
                    playersType.update({i: Player() if i == 0 else NPC()})
                case 3: # NPC VS NPC
                    playersType.update({i: NPC()})
                case _: # Игрок VS Игрок
                    playersType.update({i: Player()})

        #тело Игры
        endGame = 0
        while endGame != 1:

            # Встряхиваем сумку с бочонками
            tub = new_generator.mixBag()

            # Выводим номер выпавшего бочонка и сколько бочонков в мешке
            print(f'Новый бочонок: {tub} (осталось {len(new_generator.poolList)})')

            # Печатаем карты игроков
            for k,v in playersCard.items():
                v.printCard(f'Карта игрока №{k +1}')

            # Проверяем ответы игроков и модифицируем карты
            for i in range(numPlayer):

                # Задаем вопрос игроку и получаем ответ
                answPlayers =''
                while 'да' != answPlayers != 'нет':
                    print(f'Игрок №{i +1} Зачеркнуть цифру {tub} (да/нет)?')
                    answPlayers = playersType[i].getAnswer(tub, playersCard[i].getCardInfo)
                resultModif = playersCard[i].modifyCard(tub)

                # Проверяем проиграл ли игрок
                if resultModif != (answPlayers == 'да'):
                    print(f'Игрок №{i + 1} проиграл!')
                    endGame = 1
                    break

                # Проверяем победил ли данный игрок
                if playersType[i].win(playersCard[i].getCardInfo):
                    print(f'\n\bИгрок №{i +1} победил!')
                    playersCard[i].printCard(f'Карта игрока №{k + 1}')
                    endGame = 1
                    break