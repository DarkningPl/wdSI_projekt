import fileinput
import random

from mapdata import *
from queue import Queue


CARDS = ["red", "dodgerblue", "yellow", "white", "darkviolet", "darkorange", "hotpink", "lawngreen", "silver"]
# States of the game:
# "wait" - game waits for action from the player, second value is None
# "take" - player chooses cards out of the 5 visible ones on the table, second value is cards remaining to choose
# "initial_discard" - player chooses objectives to discard, second value is how many more can be discarded
# "discard" - player chooses new objectives to discard, second value is how many more can be discarded
# "build" - player attempts to build a connection between cities


def isObjectiveInList(objective, collection):
    t1 = objective.text1.getText()
    t2 = objective.text2.getText()
    for c in collection:
        if (t1 == getCities()[c[0]] and t2 == getCities()[c[1]]) or (t1 == getCities()[c[1]] and t2 == getCities()[c[0]]):
            return True
    return False


def initializeBoard(board):
    # Dodanie przycisków
    board.buttons.append(("names_toggle", Button(Rectangle(Point(0-.5, 860-.5), Point(180-.5, 900-.5)),
                                                 Text(Point(90-.5, 880-.5), "Wyświetlaj nazwy miast"), bColor="Yellow")))
    board.buttons.append(("quit", Button(Rectangle(Point(1680-.5, 0-.5), Point(1800-.5, 40-.5)),
                                         Text(Point(1740-.5, 20-.5), "Wyjdź z gry"), bColor="teal")))
    board.buttons.append(("start", Button(Rectangle(Point(1400-.5, 0-.5), Point(1520-.5, 40-.5)),
                                          Text(Point(1460-.5, 20-.5), "Rozpocznij grę"), bColor="peachpuff")))
    board.buttons.append(("take_cards", Button(Rectangle(Point(-600-.5, 860-.5), Point(-400-.5, 900-.5)),
                                               Text(Point(-500-.5, 880-.5), "Weź karty ze stosu"), bColor="aquamarine")))
    board.buttons.append(("take_vis_cards", Button(Rectangle(Point(-600-.5, 820-.5), Point(-400-.5, 860-.5)),
                                                   Text(Point(-500-.5, 840-.5), "Weź karty ze stołu"), bColor="aquamarine")))
    board.buttons.append(("take_objectives", Button(Rectangle(Point(-600-.5, 780-.5), Point(-400-.5, 820-.5)),
                                                    Text(Point(-500-.5, 800-.5), "Weź karty celów"), bColor="aquamarine")))
    board.buttons.append(("build", Button(Rectangle(Point(-400-.5, 860-.5), Point(-200-.5, 900-.5)),
                                          Text(Point(-300-.5, 880-.5), "Zbuduj połączenie"), bColor="aquamarine")))
    board.buttons.append(("pass", Button(Rectangle(Point(-400-.5, 820-.5), Point(-200-.5, 860-.5)),
                                         Text(Point(-300-.5, 840-.5), "Pas"), bColor="aquamarine")))
    board.buttons.append(("continue", Button(Rectangle(Point(-400-.5, 780-.5), Point(-200-.5, 820-.5)),
                                             Text(Point(-300-.5, 800-.5), "Kontynuuj"), bColor="aquamarine")))

    for i in range(8):
        for j in range(12):
            board.all_cards[0].append((CARDS[i], j))
            rect = Rectangle(Point(-80, -80), Point(-40, -20))
            rect.draw(board.win)
            board.all_cards[1].append((rect, True))
    for j in range(14):
        board.all_cards[0].append((CARDS[8], j))
        rect = Rectangle(Point(-80, -80), Point(-40, -20))
        rect.draw(board.win)
        board.all_cards[1].append((rect, True))                                                    # DONE

    for i in range(len(board.all_objectives[0])):
        obj_list = []
        copy = []
        if i == 0:
            for j in board.all_objectives[0][i]:
                o_card = ObjectiveCard(j, None)
                o_card.draw(board.win)
                obj_list.append(o_card)
                copy.insert(random.randint(0, len(copy)), j)
        elif i == 1:
            for j in board.all_objectives[0][i]:
                o_card = ObjectiveCard(j, None, color="aliceblue")
                o_card.draw(board.win)
                obj_list.append(o_card)
                copy.insert(random.randint(0, len(copy)), j)
        board.all_objectives[1].append(obj_list)
        board.available_objectives.append(copy)  # DONE

    # Rysowanie połączeń
    board.allConns.makeConnections()
    board.allConns.draw(board.win)

    # Rysowanie miast
    for i in board.cities[0]:
        x, y = i.location
        name = i.name
        text = Text(Point(x, y + 20), name)
        circle = Circle(Point(x, y), 8)
        circle.setFill("lime")
        circle.setWidth(1)
        circle.draw(board.win)
        text.draw(board.win)
        board.cities[1].append(circle)
        board.cities[2].append(text)                                                  # DONE

    # Implementacja przycisków
    for b in board.buttons:
        key, but = b
        but.draw(board.win)                                                          # DONE

    #Implementacja konsoli
    for i in range(5):
        txt = Text(Point(1540, 20 + i * 20), "")
        txt.setSize(8)
        txt.draw(board.win)
        board.console.append(txt)                                                   # DONE

    # Rozdanie kart
    for i in range(len(board.all_cards[0])):
        board.available_cards.insert(random.randint(0, len(board.available_cards)), board.all_cards[0][i])
    for i in range(5):
        board.visible_cards.append(board.available_cards.pop(0))
    for i in range(4):
        board.player.giveCard(board.available_cards.pop(0))
        board.bot.giveCard(board.available_cards.pop(0))

    board.player.giveObjective(board.available_objectives[1].pop(0))
    board.bot.giveObjective(board.available_objectives[1].pop(0))
    for i in range(3):
        board.player.giveObjective(board.available_objectives[0].pop(0))
        board.bot.giveObjective(board.available_objectives[0].pop(0))

    board.wait.setSize(30)
    board.wait.setFill("ivory")
    board.wait.draw(board.win)
    board.lastTurnMsg.setSize(24)
    for i in board.scoreTxt:
        i.setFill("ivory")
        i.draw(board.win)
    for i in board.scoreVal:
        i.setFill("ivory")
        i.draw(board.win)


def updateBoard(board):
    # View state in exiting window
    mouse_pos = board.win.checkMouse()
    if mouse_pos is not None:
        checkMouseClicks(board, mouse_pos)

    # =================================================================================================================

    # Gra w toku
    if board.gameBegun:
        # Przetasowanie widocznych kart na wypadek 3 lub więcej kart z lokomotywą
        silver_cards = 0
        for i, _ in board.visible_cards:
            if i == "silver":
                silver_cards = silver_cards + 1
        if silver_cards >= 3:
            for i in range(5):
                board.available_cards.insert(random.randint(int(len(board.available_cards) / 2), len(board.available_cards)), board.visible_cards.pop(0))

        # Dobieranie kart ze stosu aby zawsze było 5 widocznych na stole
        if len(board.visible_cards) < 5:
            i = 5 - len(board.visible_cards)
            while len(board.available_cards) > 0 and i > 0:
                board.visible_cards.append(board.available_cards.pop(0))
                i = i - 1
            board.cardsNeedUpdate = True

        # Wejście w ostatnią turę gry
        if (board.player.wagons <= 2 or board.bot.wagons <= 2) and not board.lastTurn:
            board.lastTurn = True
            board.lastTurnMsg.draw(board.win)

        # Zakończenie gry
        if board.lastTurn and board.lastMoves <= 0 and not board.gameOver:
            board.gameOver = True
            board.lastTurnMsg.setFill("ivory")
            board.gameOverMsg.draw(board.win)
            board.winnerMsg.draw(board.win)
            winner = ""
            if board.player.countScore(True) > board.bot.countScore(True):
                winner = "gracz"
            elif board.player.countScore(True) < board.bot.countScore(True):
                winner = "bot"
            if winner == "":
                board.winnerMsg.setText("Remis!")
            else:
                board.winnerMsg.setText("Wygrywa " + winner + "!")
            for i in board.buttons:
                if i[0] == "take_cards" or i[0] == "take_vis_cards" or i[0] == "take_objectives" or i[0] == "build" or i[0] == "pass" or i[0] == "continue":
                    i[1].move(-2000, 0)

        # Ruch gracza
        if board.playerTurn:
            if board.state[0] == "build":
                if board.state[1] == 2:
                    if len(board.temporary_cards) < 3:
                        i = 3 - len(board.temporary_cards)
                        while len(board.available_cards) > 0 and i > 0:
                            board.temporary_cards.append(board.available_cards.pop(0))
                            i = i - 1
                        board.cardsNeedUpdate = True
                        board.state = ("build", 3)
                elif board.state[1] == 3:
                    k = board.player.targetConnection[0].checkForBuilding(board.player, board.player.targetConnection[1], extras=board.temporary_cards)
                    if k is None:
                        updateConsole(board, "Nie można zbudować drogi")
                        board.state = ("build", 0)
                    else:
                        updateConsole(board, "Zbudować drogę z " + str(k[0]) + " koloru i " + str(k[1]) + " srebrnych?")
                        board.state = ("build", 4)
        # Ruch bota
        else:
            board.bot.sendInformation((board.state, board.allConns, board.visible_cards))
            move = board.bot.getMove()

            if move is not None:
                if move[0] == "pas":
                    updateConsole(board, "Bot pasuje")
                    updateConsole(board, "Twój ruch!")
                    board.playerTurn = True
                    board.state = "wait", None
                    if board.lastTurn:
                        board.lastMoves -= 1
                elif move[0] == "takepile":
                    for j in range(2):
                        if len(board.available_cards) > 0:
                            board.bot.giveCard(board.available_cards.pop(0))
                    updateConsole(board, "Bot bierze karty ze stosu")
                    updateConsole(board, "Twój ruch!")
                    board.playerTurn = True
                    if board.lastTurn:
                        board.lastMoves -= 1
                elif move[0] == "takevis":
                    if board.state[0] == "wait":
                        board.state = "take", 2
                    if move[1] == "silver":
                        board.state = board.state[0], board.state[1] - 2
                        card = None
                        for i in board.visible_cards:
                            if i[0] == move[1]:
                                card = i
                                break
                        if card is not None:
                            board.bot.giveCard(card)
                            if card in board.visible_cards:
                                board.visible_cards.remove(card)
                            board.visible_cards.append(board.available_cards.pop(0))
                    else:
                        board.state = board.state[0], board.state[1] - 1
                        card = None
                        for i in board.visible_cards:
                            if i[0] == move[1]:
                                card = i
                                break
                        if card is not None:
                            board.bot.giveCard(card)
                            if card in board.visible_cards:
                                board.visible_cards.remove(card)
                            board.visible_cards.append(board.available_cards.pop(0))
                    updateConsole(board, "Bot bierze kartę ze stołu")
                elif move[0] == "takeobj":
                    for i in range(3):
                        board.bot.temporaryObjectives.append(board.available_objectives[0].pop(0))
                    board.state = ("discard", 2)
                    board.cardsNeedUpdate = True
                elif move[0] == "discard":
                    for i in move[1]:
                        board.objectives_to_retrieve.append(i)
                    for j in board.objectives_to_retrieve:
                        if j in board.bot.temporaryObjectives:
                            board.bot.temporaryObjectives.remove(j)
                        board.available_objectives[1].insert(random.randint(int(len(board.available_objectives[1]) / 2), len(board.available_objectives[1])), j)
                    board.objectives_to_retrieve.clear()
                elif move[0] == "build":
                    con = board.bot.targetConnection[0]
                    if board.state[0] == "wait":
                        if con.roadType != "train" and con.special != 1:
                            if len(board.temporary_cards) < 3:
                                i = 3 - len(board.temporary_cards)
                                while len(board.available_cards) > 0 and i > 0:
                                    board.temporary_cards.append(board.available_cards.pop(0))
                                    i = i - 1
                        k = con.checkForBuilding(board.bot, move[1], extras=board.temporary_cards)
                        board.state = ("build", k)
                        updateConsole(board, "Bot próbuje zbudować drogę " + con.cities[0].name + " - " + con.cities[1].name)
                    else:
                        cardsToRemove = []
                        for j in board.bot.cards:
                            if board.state[1][0] > 0:
                                if j[0] == board.bot.targetConnection[1]:
                                    cardsToRemove.append(j)
                                    board.state = (board.state[0], (board.state[1][0] - 1, board.state[1][1]))
                            elif board.state[1][0] > 0:
                                if j[0] == "silver":
                                    cardsToRemove.append(j)
                                    board.state = (board.state[0], (board.state[1][0], board.state[1][1] - 1))
                            else:
                                continue
                        for j in board.temporary_cards:
                            cardsToRemove.append(j)
                        for j in cardsToRemove:
                            board.available_cards.insert(random.randint(int(len(board.available_cards) / 2), len(board.available_cards)), j)
                            if j in board.bot.cards:
                                board.bot.cards.remove(j)
                            elif j in board.temporary_cards:
                                board.temporary_cards.remove(j)
                        board.bot.targetConnection[0].buildConnection(board.bot)
                        if board.names_visible:
                            refreshCityNames(board)
                        board.bot.wagons = board.bot.wagons - board.bot.targetConnection[0].roadLength
                        board.bot.targetConnection = None
                        board.state = ("wait", None)
                        updateConsole(board, "Bot buduje drogę " + con.cities[0].name + " - " + con.cities[1].name)
                        updateConsole(board, "Twój ruch!")
                        board.playerTurn = True
                        if board.lastTurn:
                            board.lastMoves -= 1
            # Oddanie zbędnych kart na stos
            count = range(len(board.player.discardedCards))
            for i in count:
                board.available_cards.insert(random.randint(int(len(board.available_cards) / 2), len(board.available_cards)), board.player.discardedCards.pop(0))
            count = range(len(board.bot.discardedCards))
            for i in count:
                board.available_cards.insert(random.randint(int(len(board.available_cards) / 2), len(board.available_cards)), board.bot.discardedCards.pop(0))

            updateCards(board)

        if board.state == ("take", 0):
            if board.playerTurn:
                updateConsole(board, "Ruch bota!")
                board.playerTurn = False
            else:
                updateConsole(board, "Twój ruch!")
                board.playerTurn = True
            if board.lastTurn:
                board.lastMoves -= 1
            board.state = ("wait", None)
        if board.cardsNeedUpdate:
            updateCards(board)


def checkMouseClicks(board, mouse_pos):
    # Przyciski
    for i in range(len(board.buttons)):
        key, but = board.buttons[i]
        if recContainsPoint(mouse_pos, but.getBox()):
            if key == "names_toggle":
                board.names_visible = not board.names_visible
                if board.names_visible:
                    for c in board.cities[2]:
                        c.draw(board.win)
                else:
                    for c in board.cities[2]:
                        c.undraw()
            if key == "quit":
                board.win.close()
            if key == "start":
                board.gameBegun = True
                but.undraw()
                updateCards(board)
                for b in board.buttons:
                    if b[0] == "take_cards" or b[0] == "take_vis_cards" or b[0] == "take_objectives" \
                            or b[0] == "build" or b[0] == "pass" or b[0] == "continue":
                        b[1].move(2000, 0)
                board.state = ("initial_discard", 2)
                updateConsole(board, "Odrzuć maksymalnie 2 cele i kontynuuj")
                for j in board.scoreTxt:
                    j.setFill("black")
                for j in range(len(board.scoreVal)):
                    board.scoreVal[j].setFill("black")
                    if j == 0:
                        board.scoreVal[j].setText(board.player.countScore())
                    if j == 1:
                        board.scoreVal[j].setText(board.player.wagons)
                    if j == 2:
                        board.scoreVal[j].setText(board.bot.countScore())
                    if j == 3:
                        board.scoreVal[j].setText(board.bot.wagons)
            if key == "take_cards":
                if board.gameBegun and board.playerTurn and board.state[0] == "wait":
                    for j in range(2):
                        if len(board.available_cards) > 0:
                            board.player.giveCard(board.available_cards.pop(0))
                    board.cardsNeedUpdate = True
                    for j in range(len(board.all_cards[0])):
                        if board.all_cards[0][j] in board.available_cards or board.all_cards[0][j] in board.player.cards:
                            board.all_cards[1][j] = (board.all_cards[1][j][0], True)
                    updateConsole(board, "Zabrano 2 karty ze stosu!")
                    updateConsole(board, "Ruch bota!")
                    board.playerTurn = False
                    if board.lastTurn:
                        board.lastMoves -= 1
            if key == "take_vis_cards":
                if board.gameBegun and board.playerTurn and board.state[0] == "wait":
                    board.state = ("take", 2)
                    updateConsole(board, "Dobierz karty")
            if key == "take_objectives":
                if board.gameBegun and board.playerTurn and board.state[0] == "wait":
                    if len(board.player.objectives) > 5:
                        updateConsole(board, "Nie można dobrać więcej celów")
                    else:
                        for j in range(3):
                            board.player.temporaryObjectives.append(board.available_objectives[0].pop(0))
                        board.state = ("discard", 2)
                        board.cardsNeedUpdate = True
            if key == "build":
                if board.gameBegun and board.playerTurn:
                    if board.state[0] == "wait":
                        board.state = ("build", 0)
                        updateConsole(board, "Wybierz drogę do zbudowania")
                    if board.state == ("build", 4):
                        if board.player.targetConnection is not None:
                            pol = board.player.targetConnection[0].checkForBuilding(board.player, board.player.targetConnection[1], board.temporary_cards)
                            if pol is not None:
                                col, sil = pol
                                if countCards(board.player.cards, board.player.targetConnection[1]) >= col and countCards(board.player.cards, "silver") >= sil:
                                    cardsToRemove = []
                                    for j in board.player.cards:
                                        if col > 0:
                                            if j[0] == board.player.targetConnection[1]:
                                                cardsToRemove.append(j)
                                                col = col - 1
                                        elif sil > 0:
                                            if j[0] == "silver":
                                                cardsToRemove.append(j)
                                                sil = sil - 1
                                        else:
                                            continue
                                    for j in board.temporary_cards:
                                        cardsToRemove.append(j)
                                    for j in cardsToRemove:
                                        board.available_cards.insert(random.randint(int(len(board.available_cards) / 2), len(board.available_cards)), j)
                                        if j in board.player.cards:
                                            board.player.cards.remove(j)
                                        elif j in board.temporary_cards:
                                            board.temporary_cards.remove(j)
                                    board.player.targetConnection[0].buildConnection(board.player)
                                    if board.names_visible:
                                        refreshCityNames(board)
                                    board.player.wagons = board.player.wagons - board.player.targetConnection[0].roadLength
                                    board.player.targetConnection = None
                                    board.state = ("wait", None)
                                    board.cardsNeedUpdate = True
                                else:
                                    updateConsole(board, "Nie można zbudować drogi")
                        updateConsole(board, "Ruch bota!")
                        board.playerTurn = False
                        if board.lastTurn:
                            board.lastMoves -= 1
            if key == "pass":
                if board.gameBegun and board.playerTurn:
                    if board.state[0] != "initial_discard" and board.state[0] != "discard":
                        if board.state == ("build", 4):
                            cardsToRemove = []
                            for j in board.temporary_cards:
                                cardsToRemove.append(j)
                            for j in cardsToRemove:
                                board.available_cards.insert(random.randint(int(len(board.available_cards) / 2), len(board.available_cards)), j)
                                if j in board.temporary_cards:
                                    board.temporary_cards.remove(j)
                            board.cardsNeedUpdate = True
                            board.player.targetConnection = None
                        board.state = ("wait", None)
                        updateConsole(board, "Gracz pasuje")
                        updateConsole(board, "Ruch bota!")
                        board.playerTurn = False
                        if board.lastTurn:
                            board.lastMoves -= 1
            if key == "continue":
                if board.gameBegun and board.playerTurn:
                    if board.state[0] == "initial_discard":
                        # TODO take bot's discarded objectives
                        for j in board.objectives_to_retrieve:
                            if j in board.player.temporaryObjectives:
                                board.player.temporaryObjectives.remove(j)
                            if j in board.bot.temporaryObjectives:
                                board.bot.temporaryObjectives.remove(j)
                            if j[2] < 20:
                                board.available_objectives[0].insert(
                                    random.randint(int(len(board.available_objectives[0]) / 2),
                                                   len(board.available_objectives[0])), j)
                            else:
                                board.available_objectives[1].insert(
                                    random.randint(int(len(board.available_objectives[1]) / 2),
                                                   len(board.available_objectives[1])), j)
                        board.objectives_to_retrieve.clear()
                        board.player.confirmObjectives()
                        board.bot.confirmObjectives()
                        board.cardsNeedUpdate = True
                        for k in board.cities[1]:
                            k.setFill("lime")
                        board.state = ("wait", None)
                        updateConsole(board, "Twój ruch!")
                    elif board.state[0] == "discard":
                        for j in board.objectives_to_retrieve:
                            board.player.temporaryObjectives.remove(j)
                            if j[2] < 20:
                                board.available_objectives[0].insert(
                                    random.randint(int(len(board.available_objectives[0]) / 2),
                                                   len(board.available_objectives[0])), j)
                            else:
                                board.available_objectives[1].insert(
                                    random.randint(int(len(board.available_objectives[1]) / 2),
                                                   len(board.available_objectives[1])), j)
                        board.objectives_to_retrieve.clear()
                        board.player.confirmObjectives()
                        board.cardsNeedUpdate = True
                        for k in board.cities[1]:
                            k.setFill("lime")
                        board.state = ("wait", None)
                        updateConsole(board, "Ruch bota!")
                        board.playerTurn = False
                        if board.lastTurn:
                            board.lastMoves -= 1

            # add other button functions

    # Odsłonięte karty
    for i in range(len(board.all_cards[0])):
        j = len(board.all_cards[0]) - 1 - i
        if board.all_cards[0][j] in board.visible_cards:
            if recContainsPoint(mouse_pos, board.all_cards[1][j][0]):
                if board.playerTurn and board.state[0] == "take":
                    if board.all_cards[0][j][0] == "silver":
                        if board.state[1] >= 2:
                            board.state = ("take", board.state[1] - 2)
                            board.player.giveCard(board.all_cards[0][j])
                            board.visible_cards.remove(board.all_cards[0][j])
                    else:
                        if board.state[1] >= 1:
                            board.state = ("take", board.state[1] - 1)
                            board.player.giveCard(board.all_cards[0][j])
                            board.visible_cards.remove(board.all_cards[0][j])
        if board.all_cards[0][j] in board.player.cards:
            if recContainsPoint(mouse_pos, board.all_cards[1][j][0]):
                if board.gameBegun and board.state == ("build", 1):
                    if board.playerTurn:
                        if board.player.targetConnection[0].roadType == "double":
                            if board.all_cards[0][j][0] == board.player.targetConnection[0].color[0].value:
                                board.player.targetConnection = (board.player.targetConnection[0], board.player.targetConnection[0].color[0].value)
                                updateConsole(board, "Wybrano kolor " + board.player.targetConnection[0].color[0].value)
                                if board.player.targetConnection[0].special != 1:
                                    board.state = ("build", 2)
                                else:
                                    board.state = ("build", 3)
                                break
                            elif board.all_cards[0][j][0] == board.player.targetConnection[0].color[1].value:
                                board.player.targetConnection = (board.player.targetConnection[0], board.player.targetConnection[0].color[1].value)
                                updateConsole(board, "Wybrano kolor " + board.player.targetConnection[0].color[1].value)
                                if board.player.targetConnection[0].special != 1:
                                    board.state = ("build", 2)
                                else:
                                    board.state = ("build", 3)
                                break
                            else:
                                updateConsole(board, "Nie można użyć tego koloru")
                        elif board.player.targetConnection[0].roadType == "single":
                            for k in COLORS:
                                if k.value == board.all_cards[0][j][0]:
                                    board.player.targetConnection = (board.player.targetConnection[0], k.value)
                                    updateConsole(board, "Wybrano kolor " + str(k.value))
                                    if board.player.targetConnection[0].special != 1:
                                        board.state = ("build", 2)
                                    else:
                                        board.state = ("build", 3)
                                    break
                        else:
                            for k in COLORS:
                                if k.value == board.all_cards[0][j][0]:
                                    board.player.targetConnection = (board.player.targetConnection[0], k.value)
                                    updateConsole(board, "Wybrano kolor " + str(k.value))
                                    board.state = ("build", 3)
                                    break
                    # Tura bota TODO
                    else:
                        pass

    # Wybranie połączenia
    for c in board.allConns.connections:
        for r in c.roads:
            if roadContainsPoint(mouse_pos, r):
                if board.gameBegun and board.playerTurn and board.state == ("build", 0):
                    updateConsole(board, "Wybrana droga: " + c.cities[0].name + " - " + c.cities[1].name)
                    if c.roadType == "single" and c.color[0] != COLORS.SIL:
                        board.player.targetConnection = (c, c.color[0].value)
                        if c.special != 1:
                            board.state = ("build", 2)
                        else:
                            board.state = ("build", 3)
                    else:
                        if c.roadType == "double" and countCards(board.player.cards, c.color[0].value) < c.roadLength and countCards(board.player.cards, c.color[1].value) < c.roadLength:
                            board.state = ("build", 3)
                        else:
                            board.state = ("build", 1)
                            board.player.targetConnection = (c, None)
                            updateConsole(board, "Wybierz kolor")

    # Kliknięcie karty celu
    for i in range(len(board.all_objectives[1])):
        for j in range(len(board.all_objectives[1][i])):
            obj = (board.all_objectives[0][i][j], board.all_objectives[1][i][j])
            if recContainsPoint(mouse_pos, obj[1].box):
                if obj[0] in board.player.temporaryObjectives:
                    for k in range(len(board.cities[0])):
                        if board.cities[0][k].name == obj[1].text1.getText() or board.cities[0][k].name == obj[1].text2.getText():
                            # board.cities[1][k] = Circle(board.cities[1][k].getCenter(), 12)
                            board.cities[1][k].setFill("goldenrod")
                        else:
                            # board.cities[1][k] = Circle(board.cities[1][k].getCenter(), 8)
                            board.cities[1][k].setFill("lime")
                    if board.state[0] == "initial_discard" or board.state[0] == "discard":
                        if obj[0] not in board.objectives_to_retrieve:
                            board.objectives_to_retrieve.append(obj[0])
                            obj[1].box.setFill("tomato")
                            board.state = (board.state[0], board.state[1] - 1)
                        else:
                            board.objectives_to_retrieve.remove(obj[0])
                            obj[1].box.setFill(obj[1].color)
                            board.state = (board.state[0], board.state[1] + 1)
                            for k in board.cities[1]:
                                # k = Circle(k.getCenter(), 8)
                                k.setFill("lime")
                elif obj[0] in board.player.objectives:
                    for k in range(len(board.cities[0])):
                        if board.cities[0][k].name == obj[1].text1.getText() or board.cities[0][k].name == obj[1].text2.getText():
                            board.cities[1][k].setFill("goldenrod")
                        else:
                            board.cities[1][k].setFill("lime")


def updateCards(board):
    board.wait.setFill("black")
    distribution = [[], [], [], [], []]
    for i in range(len(board.all_cards[0])):
        c = (board.all_cards[0][i], board.all_cards[1][i])
        if c[0] in board.available_cards:
            distribution[0].append(c)
        elif board.all_cards[0][i] in board.visible_cards:
            distribution[1].append(c)
        elif board.all_cards[0][i] in board.temporary_cards:
            distribution[2].append(c)
        elif board.all_cards[0][i] in board.player.cards:
            distribution[3].append(c)
        elif board.all_cards[0][i] in board.bot.cards:
            distribution[4].append(c)
    for i in range(len(distribution)):
        for j in range(len(distribution[i])):
            # Pile of cards
            if i == 0:
                c = distribution[i][j]
                if c[1][1]:
                    c[1][0].move(1760 + 0.1 * j - c[1][0].getCenter().x, 420 + 0.2 * j - c[1][0].getCenter().y)
                    c[1][0].setFill("chocolate")
                    distribution[i][j] = (c[0], (c[1][0], False))
            # Visible cards
            elif i == 1:
                c = distribution[i][j]
                if c[1][1]:
                    c[1][0].move(1440 + 50 * j - c[1][0].getCenter().x, 420 - c[1][0].getCenter().y)
                    c[1][0].setFill(c[0][0])
                    distribution[i][j] = (c[0], (c[1][0], False))
            # Temporary cards
            elif i == 2:
                c = distribution[i][j]
                if c[1][1]:
                    c[1][0].move(1700 - c[1][0].getCenter().x, 420 + 70 * (j - 1) - c[1][0].getCenter().y)
                    c[1][0].setFill(c[0][0])
                    distribution[i][j] = (c[0], (c[1][0], False))
            # Player cards
            elif i == 3:
                c = distribution[i][j]
                if c[1][1]:
                    denum = len(distribution[3]) - 1
                    if denum == 0:
                        offset = 0
                    else:
                        offset = 160 * (j - len(distribution[3]) / 2 + .5) / (len(distribution[3]) - 1)
                    c[1][0].move(1540 + offset - c[1][0].getCenter().x, 270 - c[1][0].getCenter().y)
                    c[1][0].setFill(c[0][0])
                    distribution[i][j] = (c[0], (c[1][0], False))
            # Bot cards
            elif i == 4:
                c = distribution[i][j]
                if c[1][1]:
                    denum = len(distribution[4]) - 1
                    if denum == 0:
                        offset = 0
                    else:
                        offset = 160 * (j - len(distribution[4]) / 2 + .5) / (len(distribution[4]) - 1)
                    c[1][0].move(1540 + offset - c[1][0].getCenter().x, 570 - c[1][0].getCenter().y)
                    c[1][0].setFill("chocolate")
                    distribution[i][j] = (c[0], (c[1][0], False))
    pass
    distribution = [[], [], [], [], []]
    for i in 0, 1:
        for j in range(len(board.all_objectives[0][i])):
            obj = (board.all_objectives[0][i][j], board.all_objectives[1][i][j])
            if obj[0] in board.available_objectives[0] or obj[0] in board.available_objectives[1]:
                distribution[0].append(obj)
            elif obj[0] in board.player.temporaryObjectives:
                distribution[1].append(obj)
            elif obj[0] in board.player.objectives:
                distribution[2].append(obj)
            elif obj[0] in board.bot.temporaryObjectives:
                distribution[3].append(obj)
            elif obj[0] in board.bot.objectives:
                distribution[4].append(obj)
    for i in range(len(distribution)):
        for j in range(len(distribution[i])):
            o_card = distribution[i][j][1]
            # Off-screen objectives
            if i == 0:
                o_card.moveTo(-100, 0)
                o_card.changeVisibility(False)
            # Player temporary objectives
            elif i == 1:
                pass
                o_card.moveTo(1460 + 80 * j, 345)
                o_card.changeVisibility(True)
            # Player objectives
            elif i == 2:
                pass
                o_card.moveTo(1740, 300 - (len(distribution[i]) - 1 - j) * 30)
                o_card.changeVisibility(True)
            # Bot temporary objectives
            elif i == 3:
                pass
                o_card.changeVisibility(False)
                o_card.moveTo(1460 + 80 * j, 495)
            # Bot objectives
            elif i == 4:
                pass
                o_card.moveTo(1740, 540 + j * 30)
                o_card.changeVisibility(False)

    for j in range(len(board.scoreVal)):
        if j == 0:
            board.scoreVal[j].setText(board.player.countScore())
        if j == 1:
            board.scoreVal[j].setText(board.player.wagons)
        if j == 2:
            board.scoreVal[j].setText(board.bot.countScore())
        if j == 3:
            board.scoreVal[j].setText(board.bot.wagons)
    board.wait.setFill("ivory")
    board.cardsNeedUpdate = False


def updateConsole(board, text):
    if board.gameBegun:
        for i in board.console:
            temp = i.getText()
            i.setText(text)
            text = temp


def refreshCityNames(board):
    for i in board.cities[2]:
        i.undraw()
        i.draw(board.win)


class Player:

    def __init__(self, color):
        self.wagons = 45
        self.cards = []
        self.objectives = []
        self.temporaryObjectives = []
        self.discardedCards = []
        self.discardedObjectives = []
        self.claimedConnections = []
        self.color = color
        self.targetConnection = None
        self.info = None

    def giveCard(self, card):
        index = 0
        for c in CARDS:
            if card[0] == c:
                break
            index = index + countCards(self.cards, c)

        self.cards.insert(index, card)
        pass

    def giveObjective(self, card):
        self.temporaryObjectives.append(card)

    def countScore(self, finished=False):
        score = 0
        roads = {getCities()[n].name: [] for n in range(len(getCities()))}
        for c in self.claimedConnections:
            dlug = c.roadLength
            if dlug == 8:
                score = score + 21
            elif dlug == 6:
                score = score + 15
            elif dlug == 4:
                score = score + 7
            elif dlug == 3:
                score = score + 4
            else:
                score = score + dlug
            roads[c.cities[0].name].append(c.cities[1].name)
            roads[c.cities[1].name].append(c.cities[0].name)

        for obj in self.objectives:
            if checkObjective(obj, roads):
                score = score + obj[2]
            elif finished:
                score = score - obj[2]

        return score

    def confirmObjectives(self):
        for i in self.temporaryObjectives:
            self.objectives.append(i)
        self.temporaryObjectives.clear()


from agent import Agent


class Board:
    def __init__(self, title="Wsiasc do pociagu"):
        win = self.win = GraphWin(title, 1800, 900)
        win.setBackground("ivory")
        win.setCoords(-.5, -.5, 1800 - .5, 900 - .5)
        background = Image(Point(700 - 0.5, 450 - .5), "./real_map_cropped.png")
        background.draw(win)

        self.cities = [getCities(), [], []]
        self.city_names = []
        self.names_visible = True
        self.allConns = Connections()
        self.player = Player("turquoise")
        self.bot = Agent("indianred")
        self.quit = False
        self.gameBegun = False
        self.gameOver = False
        self.lastTurn = False
        self.lastMoves = 2
        self.playerTurn = True
        self.cardsNeedUpdate = False
        self.buttons = []
        self.all_cards = [[], []]
        self.all_objectives = [getObjectives(), []]
        self.available_cards = []
        self.available_objectives = []

        self.cards = []
        self.visible_cards = []
        self.temporary_cards = []
        self.rendered_cards = []
        self.objectives = getObjectives()
        self.rendered_objectives = []
        self.console = []
        self.objectives_to_retrieve = []
        self.wait = Text(Point(1540, 150), "Czekaj")
        self.lastTurnMsg = Text(Point(1540, 700), "Ostatnia tura!")
        self.gameOverMsg = Text(Point(1600, 840), "Koniec gry!")
        self.winnerMsg = Text(Point(1600, 780), "")
        self.scoreTxt = [Text(Point(1460, 200), "Punkty:"), Text(Point(1600, 200), "Wagony:"),
                         Text(Point(1460, 640), "Punkty:"), Text(Point(1600, 640), "Wagony:")]
        self.scoreVal = [Text(Point(1500, 200), ""), Text(Point(1640, 200), ""),
                         Text(Point(1500, 640), ""), Text(Point(1640, 640), "")]
        self.state = ("wait", None)

        initializeBoard(self)

        self.update()

    def update(self):
        updateBoard(self)

    def pause(self):
        self.win.getMouse()

    def close(self):
        self.win.close()

    def getQuit(self):
        return self.quit


class Button:
    def __init__(self, rectangle, text, bColor=None, tColor=None, fFace=None, fStyle=None):
        self.box = rectangle
        if bColor is not None:
            self.box.setFill(bColor)
        self.text = text
        if tColor is not None:
            self.text.setTextColor(tColor)
        if fFace is not None:
            self.text.setFace(fFace)
        if fStyle is not None:
            self.text.setStyle(fStyle)

    def draw(self, win):
        self.box.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.box.undraw()
        self.text.undraw()

    def move(self, dx, dy):
        self.box.move(dx, dy)
        self.text.move(dx, dy)

    def getBox(self):
        return self.box


def checkObjective(objective, roads):
    visited = []
    parent = {n: None for n in roads}
    q = Queue()
    q.put(getCities()[objective[0]].name)
    while not q.empty():
        city = q.get()
        if city in visited:
            continue
        visited.append(city)
        if city == getCities()[objective[1]].name:
            return True
        for nh in roads[city]:
            if nh in visited:
                continue
            parent[nh] = city
            q.put(nh)
    return False


class ObjectiveCard:
    def __init__(self, objective, owner, color="cornsilk"):
        self.objective = objective
        self.color = color
        self.owner = owner
        self.box = Rectangle(Point(-140, 5), Point(-60, 35))
        self.box.setFill(self.color)
        self.text1 = Text(Point(-110, 27), getCities()[objective[0]].name)
        self.text1.setSize(8)
        self.text2 = Text(Point(-110, 13), getCities()[objective[1]].name)
        self.text2.setSize(8)
        self.score = Text(Point(-70, 20), str(objective[2]))

    def draw(self, win):
        self.box.draw(win)
        self.text1.draw(win)
        self.text2.draw(win)
        self.score.draw(win)

    def moveTo(self, x, y):
        center = self.box.getCenter()
        self.box.move(x-center.x, y-center.y)
        self.text1.move(x-center.x, y-center.y)
        self.text2.move(x-center.x, y-center.y)
        self.score.move(x-center.x, y-center.y)

    def getCenter(self):
        return self.box.getCenter()

    def giveTo(self, newOwner):
        self.owner = newOwner

    def returnToPile(self):
        self.giveTo(None)

    def changeVisibility(self, revealed):
        if revealed:
            self.box.setFill(self.color)
            self.text1.setFill("black")
            self.text2.setFill("black")
            self.score.setFill("black")
        else:
            self.box.setFill("chocolate")
            self.text1.setFill("chocolate")
            self.text2.setFill("chocolate")
            self.score.setFill("chocolate")
