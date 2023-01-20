# prob.py
# This is
import math
import random
import numpy as np
import queue

# from gridutil import *
from env import Player
from mapdata import *

#Tworzymy klasę Agent, który jest graczem 
class Agent(Player):
    Actions = "pas", "takevis", "takepile", "takeobj", "build", "discard"

    def getMove(self):
        stan = self.info[0]
        connections = self.info[1]
        visibles = self.info[2]
        tri = [[], [], []]  # cel, najkrotsza droga, polaczenia
        graf = getGraph(connections.connections, bot=self)
        colors = ["red", "dodgerblue", "yellow", "white", "darkviolet", "darkorange", "hotpink", "lawngreen"]
        for i in range(len(self.objectives)):
            index = 0
            for j in range(len(tri[0])):
                if tri[0][j][2] > self.objectives[i][2]:
                    index = index + 1
                else:
                    continue
            tri[0].insert(index, self.objectives[i])
            tri[1].insert(index, self.findPath(connections.connections, self.objectives[i]))
        for i in range(len(tri[1])):
            if tri[1][i] is not None:
                conns = []
                for j in range(len(tri[1][i]) - 1):
                    miasto1 = getCities()[tri[1][i][j]]
                    miasto2 = getCities()[tri[1][i][j + 1]]
                    conns.append(connections.getConnection(miasto1, miasto2))
                tri[2].append(conns)
            else:
                tri[2].append(None)
        # W tym miejscu mamy tri, zawiera cele (malejąco), odpowiadające im najkrótsze trasy i połączenia w tych trasach

        targetConn = None
        targetConns = []
        for i in range(len(tri[2])):
            for j in range(len(tri[2][i])):
                if tri[2][i][j] in self.claimedConnections:
                    continue
                else:
                    # Największy priorytet
                    if len(graf[tri[1][i][j]]) < 2 or len(graf[tri[1][i][j + 1]]) < 2:
                        targetConn = tri[2][i][j]
                        targetConns.clear()
                        targetConns.append(tri[2][i][j])
                        break
                    if targetConn is not None:
                        typ = targetConn.roadType
                        if typ == "single" and targetConn.color[0] == COLORS.SIL:
                            if tri[2][i][j].roadType == "train" or tri[2][i][j].roadType == "double" or (tri[2][i][j].roadType == "single" and tri[2][i][j].color[0] != COLORS.SIL):
                                targetConn = tri[2][i][j]
                                targetConns.clear()
                                targetConns.append(tri[2][i][j])
                            elif tri[2][i][j].roadType == "single" and tri[2][i][j].color[0] == COLORS.SIL:
                                targetConns.append(tri[2][i][j])
                        elif typ == "train":
                            if tri[2][i][j].roadType == "double" or (tri[2][i][j].roadType == "single" and tri[2][i][j].color[0] != COLORS.SIL):
                                targetConn = tri[2][i][j]
                                targetConns.clear()
                                targetConns.append(tri[2][i][j])
                            elif tri[2][i][j].roadType == "train":
                                targetConns.append(tri[2][i][j])
                        elif typ == "double":
                            if tri[2][i][j].roadType == "single" and tri[2][i][j].color[0] != COLORS.SIL:
                                targetConn = tri[2][i][j]
                                targetConns.clear()
                                targetConns.append(tri[2][i][j])
                            elif tri[2][i][j].roadType == "double":
                                targetConns.append(tri[2][i][j])
                        else:
                            if tri[2][i][j].roadType == "single" and tri[2][i][j].color[0] != COLORS.SIL:
                                targetConns.append(tri[2][i][j])
                    else:
                        targetConn = tri[2][i][j]
                        targetConns.clear()
                        targetConns.append(tri[2][i][j])
            if targetConn is not None:
                break
        # W tym miejscu mamy targetConns, czyli polaczenia, ktore w pierwszej kolejnosci chcemy wybudowac
        # (LUB targetConn jest niczym, wtedy dobieramy cele albo pasujemy, albo budujemy losowe polaczenie)

        color = None
        fewest_remaining = math.inf
        remaining = {col.value: None for col in COLORS}
        if stan[0] == "wait":
            for i in targetConns:
                hand0 = countCards(self.cards, i.color[0].value)
                if i.color[1] is not None:
                    hand1 = countCards(self.cards, i.color[1].value)
                vis0 = countCards(visibles, i.color[0].value)
                if i.color[1] is not None:
                    vis1 = countCards(visibles, i.color[1].value)
                if i.roadType == "single" and i.color[0].value != COLORS.SIL:
                    if hand0 >= i.roadLength:
                        self.targetConnection = (i, i.color[0].value)
                        return "build", i.color[0].value
                    else:  # Nie mamy wystarczajaco kart aby zbudowac polaczenie
                        if remaining[i.color[0].value] is None:
                            remaining[i.color[0].value] = i.roadLength - hand0, i.roadLength - hand0 - vis0
                        else:
                            remaining[i.color[0].value] = min(i.roadLength - hand0, remaining[i.color[0].value][0]), min(i.roadLength - hand0 - vis0, remaining[i.color[0].value][1])
                elif i.roadType == "double":
                    if hand0 >= i.roadLength:
                        self.targetConnection = (i, i.color[0].value)
                        return "build", i.color[0].value
                    else:
                        if remaining[i.color[0].value] is None:
                            remaining[i.color[0].value] = i.roadLength - hand0, i.roadLength - hand0 - vis0
                        else:
                            remaining[i.color[0].value] = min(i.roadLength - hand0, remaining[i.color[0].value][0]), min(i.roadLength - hand0 - vis0, remaining[i.color[0].value][1])
                    if hand1 >= i.roadLength:
                        self.targetConnection = (i, i.color[1].value)
                        return "build", i.color[1].value
                    else:
                        if remaining[i.color[1].value] is None:
                            remaining[i.color[1].value] = i.roadLength - hand1, i.roadLength - hand1 - vis1
                        else:
                            remaining[i.color[1].value] = min(i.roadLength - hand1, remaining[i.color[1].value][0]), min(i.roadLength - hand1 - vis1, remaining[i.color[1].value][1])
                elif i.roadType == "train":
                    pociagi = hand0 >= i.special
                    if not pociagi:
                        if vis0 >= 1:
                            return "takevis", i.color[0].value
                    for j in COLORS:
                        hand = countCards(self.cards, j.value)
                        vis = countCards(visibles, j.value)
                        if j != COLORS.SIL and j != COLORS.GRA:
                            if hand >= i.roadLength - i.special:
                                if pociagi:
                                    self.targetConnection = (i, j.value)
                                    return "build", j.value
                            else:
                                if remaining[j.value] is None:
                                    remaining[j.value] = i.roadLength - hand, i.roadLength - hand - vis
                                else:
                                    remaining[j.value] = min(i.roadLength - hand, remaining[j.value][0]), min(i.roadLength - hand - vis, remaining[j.value][1])
                else:
                    for j in COLORS:
                        hand = countCards(self.cards, j.value)
                        vis = countCards(visibles, j.value)
                        if j != COLORS.SIL and j != COLORS.GRA:
                            if hand >= i.roadLength:
                                self.targetConnection = (i, j.value)
                                return "build", j.value
                            else:
                                if remaining[j.value] is None:
                                    remaining[j.value] = i.roadLength - hand, i.roadLength - hand - vis
                                else:
                                    remaining[j.value] = min(i.roadLength - hand, remaining[j.value][0]), min(i.roadLength - hand - vis, remaining[j.value][1])
            if targetConn is None:
                return "pas", None  # W bardziej złożonym - return "takeobj", None (jeżeli ma self.objectives ma <= 5 elementów) oraz ewaluacja celów do odrzucenia
            color = None
            lowest = None
            for i in COLORS:
                if remaining[i.value] is not None:
                    if remaining[i.value][0] > 0:
                        if lowest is None:
                            lowest = remaining[i.value][1]
                            color = i.value
                        else:
                            if lowest > remaining[i.value][1]:
                                lowest = remaining[i.value][1]
                                color = i.value
            if color is None or countCards(visibles, color) == 0:
                return "takepile", None
            else:
                return "takevis", color

        if stan[0] == "take":
            for i in targetConns:
                hand0 = countCards(self.cards, i.color[0].value)
                if i.color[1] is not None:
                    hand1 = countCards(self.cards, i.color[1].value)
                vis0 = countCards(visibles, i.color[0].value)
                if i.color[1] is not None:
                    vis1 = countCards(visibles, i.color[1].value)
                if i.roadType == "single" and i.color[0].value != COLORS.SIL:
                    if remaining[i.color[0].value] is None:
                        remaining[i.color[0].value] = i.roadLength - hand0, i.roadLength - hand0 - vis0
                    else:
                        remaining[i.color[0].value] = min(i.roadLength - hand0, remaining[i.color[0].value][0]), min(i.roadLength - hand0 - vis0, remaining[i.color[0].value][1])
                elif i.roadType == "double":
                    if remaining[i.color[0].value] is None:
                        remaining[i.color[0].value] = i.roadLength - hand0, i.roadLength - hand0 - vis0
                    else:
                        remaining[i.color[0].value] = min(i.roadLength - hand0, remaining[i.color[0].value][0]), min(i.roadLength - hand0 - vis0, remaining[i.color[0].value][1])
                    if remaining[i.color[1].value] is None:
                        remaining[i.color[1].value] = i.roadLength - hand1, i.roadLength - hand1 - vis1
                    else:
                        remaining[i.color[1].value] = min(i.roadLength - hand1, remaining[i.color[1].value][0]), min(i.roadLength - hand1 - vis1, remaining[i.color[1].value][1])
                else:
                    for j in COLORS:
                        hand = countCards(self.cards, j.value)
                        vis = countCards(visibles, j.value)
                        if j != COLORS.SIL and j != COLORS.GRA:
                            if remaining[j.value] is None:
                                remaining[j.value] = i.roadLength - hand, i.roadLength - hand - vis
                            else:
                                remaining[j.value] = min(i.roadLength - hand, remaining[j.value][0]), min(i.roadLength - hand - vis, remaining[j.value][1])
            color = None
            lowest = None
            for i in COLORS:
                if remaining[i.value] is not None:
                    if remaining[i.value][0] > 0:
                        if lowest is None:
                            lowest = remaining[i.value][1]
                            color = i.value
                        else:
                            if lowest > remaining[i.value][1]:
                                lowest = remaining[i.value][1]
                                color = i.value
            if color is None:
                color = colors[random.randint(0, len(colors) - 1)]
                while countCards(visibles, color) == 0 and color != COLORS.SIL.value:
                    color = colors[random.randint(0, len(colors) - 1)]
            return "takevis", color

        if stan[0] == "discard":
            count = stan[1]  # Zaawansowane, odrzucanie niewygodnych celów
            discarded = []
            return "discard", discarded

        if stan[0] == "build":
            if stan[1] is None:
                return "pas", None
            else:
                if self.targetConnection[0].roadType != "train" and stan[1][1] > 0:
                    if random.randint(0, 1) == 0:
                        return "pas", None
                    else:
                        return "build", None
                else:
                    return "build", None

        return None

    def findPath(self, connections, objective):
        start = objective[0]
        goal = objective[1]
        graf = getGraph(connections, bot=self)
        visited = []
        parent = {loc: None for loc in range(47)}
        cost = {loc: math.inf for loc in range(47)}
        q = queue.PriorityQueue()
        q.put((0, start))
        # parent[start] = start
        cost[start] = 0
        while not q.empty():
            _, cur_n = q.get()
            if cur_n in visited:
                continue
            if cur_n == goal:
                break
            for i in graf[cur_n]:
                node, dist = i
                old_cost = cost[node]
                new_cost = cost[cur_n] + dist
                if new_cost < old_cost:
                    parent[node] = cur_n
                    cost[node] = new_cost
                q.put((cost[node], node))
            visited.append(cur_n)
        path = [goal]
        node = parent[goal]
        while node is not None:
            path.insert(0, node)
            node = parent[node]
        if len(path) > 0:
            return path
        return None

    def sendInformation(self, info):
        self.info = info  # Przesyłamy (stan planszy, wszystkie połączenia planszy, widoczne karty)
        if info is None:
            self.targetConnection = None
