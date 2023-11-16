import random

from allClases import Card
from allClases import Generator
from allClases import Player
from allClases import NPC

from allFunc import menu
from allFunc import numPlayers
from allFunc import mode

while True:
    choose = 0
    numPlayer = 0
    modeGame = 0
    # Меню
    if menu(choose) ==2:
        break
    # Выбираем количество игроков
    numPlayer = numPlayers()
    # Выбираем режим если в игре выбрано 2 игрока
    if numPlayer == 2:
        modeGame = mode()

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
    #Игра
    endGame = 0
    while endGame != 1:
        answPlayers = [i for i in range(numPlayer)]
        # Встряхиваем сумку с бочонками
        tub = new_generator.mixBag()
        # Выводим номер выпавшего бочонка и сколько бочонков в мешке
        print(f'Новый бочонок: {tub} (осталось {len(new_generator.poolList)})')
            # Печатаем карты игроков
        for k,v in playersCard.items():
                v.printCard(f'Карта игрока №{k +1}')
            # Проверяем ответы игроков и модифицируем карты
        for i in range(numPlayer):
            # Проверяем победил ли данный игрок
            if playersType[i].win(playersCard[i].cardInfo):
                print(f'Игрок №{i +1} победил!')
                endGame = 1
                break
            # Задаем вопрос игроку
            print(f'Игрок №{i +1} Зачеркнуть цифру {tub}? да/нет ')
            answPlayers[i] = playersType[i].answer(tub, playersCard[i].cardInfo)
            resultModif = playersCard[i].modifyCard(tub)
            # Анализируем ответы
            if  not(resultModif != (answPlayers[i] == 'да')):
                continue
            else:
                print(f'Игрок №{i + 1} проиграл!')
                endGame = 1
                break
