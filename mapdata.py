from graphics import *
from gridutil import *
from enum import Enum


class COLORS(Enum):
    BLU = "dodgerblue"
    GRE = "lawngreen"
    GRA = "dimgrey"
    ORA = "darkorange"
    PIN = "hotpink"
    PUR = "darkviolet"
    RED = "red"
    SIL = "silver"
    WHI = "white"
    YEL = "yellow"


def getCities():
    cities = [City("Amsterdam", (411 + 28, 1175 - 647)),     # 0
              City("Ankara", (1075 + 28, 1175 - 971)),       # 1
              City("Ateny", (850 + 28, 1175 - 1070)),        # 2
              City("Berlin", (572 + 28, 1175 - 648)),        # 3
              City("Brest", (202 + 28, 1175 - 745)),         # 4
              City("Brindisi", (704 + 28, 1175 - 1013)),     # 5
              City("Bruksela", (393 + 28, 1175 - 693)),      # 6
              City("Budapeszt", (708 + 28, 1175 - 790)),     # 7
              City("Bukareszt", (880 + 28, 1175 - 855)),     # 8
              City("Caen", (292 + 28, 1175 - 733)),          # 9
              City("Charków", (1051 + 28, 1175 - 626)),     # 10
              City("Edynburg", (268 + 28, 1175 - 510)),     # 11
              City("Erzurum", (1261 + 28, 1175 - 892)),     # 12
              City("Frankfurt", (482 + 28, 1175 - 720)),    # 13
              City("Gdańsk", (668 + 28, 1175 - 571)),       # 14
              City("Hanower", (505 + 28, 1175 - 649)),      # 15
              City("Izmir", (941 + 28, 1175 - 1047)),       # 16
              City("Kadyks", (90 + 28, 1175 - 1107)),       # 17
              City("Katania", (640 + 28, 1175 - 1118)),     # 18
              City("Kijów", (924 + 28, 1175 - 649)),        # 19
              City("Kopenhaga", (554 + 28, 1175 - 539)),    # 20
              City("Lizbona", (32 + 28, 1175 - 1022)),      # 21
              City("Londyn", (305 + 28, 1175 - 662)),       # 22
              City("Madryt", (165 + 28, 1175 - 1007)),      # 23
              City("Marsylia", (402 + 28, 1175 - 932)),     # 24
              City("Monachium", (542 + 28, 1175 - 779)),    # 25
              City("Moskwa", (960 + 28, 1175 - 480)),       # 26
              City("Pampeluna", (228 + 28, 1175 - 932)),    # 27
              City("Paryż", (355 + 28, 1175 - 744)),        # 28
              City("Petersburg", (836 + 28, 1175 - 360)),   # 29
              City("Rostów", (1136 + 28, 1175 - 688)),      # 30
              City("Ryga", (755 + 28, 1175 - 477)),         # 31
              City("Rzym", (573 + 28, 1175 - 979)),         # 32
              City("Sarajewo", (704 + 28, 1175 - 912)),     # 33
              City("Sewastopol", (1040 + 28, 1175 - 809)),  # 34
              City("Smoleńsk", (914 + 28, 1175 - 510)),     # 35
              City("Soczi", (1205 + 28, 1175 - 798)),       # 36
              City("Sofia", (838 + 28, 1175 - 922)),        # 37
              City("Stambuł", (970 + 28, 1175 - 951)),      # 38
              City("Sztokholm", (641 + 28, 1175 - 417)),    # 39
              City("Walencja", (248 + 28, 1175 - 1044)),    # 40
              City("Warszawa", (734 + 28, 1175 - 633)),     # 41
              City("Wenecja", (563 + 28, 1175 - 866)),      # 42
              City("Wiedeń", (642 + 28, 1175 - 776)),       # 43
              City("Wilno", (792 + 28, 1175 - 548)),        # 44
              City("Zagrzeb", (647 + 28, 1175 - 851)),      # 45
              City("Zurych", (479 + 28, 1175 - 810))]       # 46
    return cities


def createConnections(collection):
    #  0 Lizbona-Kadyks
    collection.append(Connection(getCities()[17], getCities()[21], color=COLORS.BLU).createRoads([(100, 93, -53), (75, 128, -54)]))
    #  1 Lizbona-Madryt
    collection.append(Connection(getCities()[21], getCities()[23], color=COLORS.PIN).createRoads([(82, 173, 38), (123, 188, 0), (164, 182, -20)]))
    #  2 Kadyks-Madryt
    collection.append(Connection(getCities()[17], getCities()[23], color=COLORS.ORA).createRoads([(147, 74, 15), (182, 98, 50), (193, 137, 90)]))
    #  3 Madryt-Walencja
    collection.append(Connection(getCities()[23], getCities()[40], color=COLORS.YEL).createRoads([(214, 149, -45), (248, 131, -5)]))
    #  4 Madryt-Pampeluna
    collection.append(Connection(getCities()[23], getCities()[27], roadType="double", color=COLORS.WHI, color2=COLORS.PUR, special=2).createRoads([(189, 196, 97), (193, 234, 54), (228, 248, -8)]))
    #  5 Walencja-Pampeluna
    collection.append(Connection(getCities()[27], getCities()[40]).createRoads([(272, 164, -80), (263, 208, -80)]))
    #  6 Walencja-Marsylia
    collection.append(Connection(getCities()[24], getCities()[40]).createRoads([(305, 143, 36), (341, 166, 39), (375, 190, 42), (409, 218, 45)]))
    #  7 Pampeluna-Marsylia
    collection.append(Connection(getCities()[24], getCities()[27], color=COLORS.RED).createRoads([(285, 243, 1), (327, 255, 20), (366, 262, -4), (405, 253, -14)]))
    #  8 Pampeluna-Paryż
    collection.append(Connection(getCities()[27], getCities()[28], roadType="double", color=COLORS.BLU, color2=COLORS.GRE).createRoads([(285, 269, 45), (320, 308, 60), (345, 351, 60), (367, 398, 62)]))
    #  9 Pampeluna-Brest
    collection.append(Connection(getCities()[4], getCities()[27], color=COLORS.PIN).createRoads([(256, 272, -89), (253, 314, -85), (246, 354, -81), (236, 398, -82)]))
    # 10 Brest-Paryż
    collection.append(Connection(getCities()[4], getCities()[28], color=COLORS.PUR).createRoads([(262, 416, -15), (310, 408, 0),(354, 415, 15) ]))
    # 11 Brest-Caen
    collection.append(Connection(getCities()[4], getCities()[9], color=COLORS.ORA).createRoads([(253, 443, 22), (293, 448, -4)]))
    # 12 Caen-Paryż
    collection.append(Connection(getCities()[9], getCities()[28], color=COLORS.PIN).createRoads([(351, 435, -9)]))
    # 13 Caen-Londyn
    collection.append(Connection(getCities()[9], getCities()[22], roadType="train").createRoads([(306, 470, -60), (305, 503, 22)]))
    # 14 Caen-Bruksela
    collection.append(Connection(getCities()[6], getCities()[9], color=COLORS.GRE).createRoads([(393, 472, 13), (351, 456, 20)]))
    # 15 Bruksela-Paryż
    collection.append(Connection(getCities()[6], getCities()[28], roadType="double", color=COLORS.YEL, color2=COLORS.RED).createRoads([(403, 456, 54)]))
    # 16 Bruksela-Amsterdam
    collection.append(Connection(getCities()[0], getCities()[6], color=COLORS.PUR).createRoads([(432, 505, 70)]))
    # 17 Amsterdam-Londyn
    collection.append(Connection(getCities()[0], getCities()[22], roadType="train", special=2).createRoads([(366, 515, 10), (410, 522, 10)]))
    # 18 Londyn-Edynburg
    collection.append(Connection(getCities()[11], getCities()[22], roadType="double", color=COLORS.ORA, color2=COLORS.PUR).createRoads([(313, 644, 130), (329, 609, 90), (322, 571, 55), (321, 534, 115)]))
    # 19 Erzurum-Ankara
    collection.append(Connection(getCities()[1], getCities()[12], color=COLORS.PUR).createRoads([(1136, 211, 20), (1180, 226, 20), (1222, 246, 30), (1261, 266, 30)]))
    # 20 Erzurum-Sewastopol
    collection.append(Connection(getCities()[12], getCities()[34], roadType="train", special=2).createRoads([(1250, 294, -20), (1204, 315, -25), (1156, 337, -30), (1106, 354, -20)]))
    # 21 Erzurum-Soczi
    collection.append(Connection(getCities()[12], getCities()[36], color=COLORS.RED).createRoads([(1290, 308, 85), (1286, 347, -75), (1258, 373, -15)]))
    # 22 Ankara-Izmir
    collection.append(Connection(getCities()[1], getCities()[16], color=COLORS.ORA, special=2).createRoads([(1082, 179, 45), (1045, 150, 30), (1001, 133, 15)]))
    # 23 Ankara-Stambuł
    collection.append(Connection(getCities()[1], getCities()[38], special=2).createRoads([(1069, 203, -5), (1026, 212, -25)]))
    # 24 Soczi-Sewastopol
    collection.append(Connection(getCities()[34], getCities()[36], roadType="train").createRoads([(1101, 375, 20), (1153, 382, 0), (1201, 380, -10)]))
    # 25 Soczi-Rostów
    collection.append(Connection(getCities()[30], getCities()[36]).createRoads([(1189, 456, -50),(1220, 412, -65) ]))
    # 26 Sewastopol-Stambuł
    collection.append(Connection(getCities()[34], getCities()[38], roadType="train", special=2).createRoads([(1056, 340, 55), (1054, 303, -75), (1051, 268, 45), (1018, 239, 40)]))
    # 27 Sewastopol-Bukareszt
    collection.append(Connection(getCities()[8], getCities()[34], color=COLORS.WHI).createRoads([(941, 331, 20), (976, 359, 60), (1006, 390, 20), (1044, 384, -40)]))
    # 28 Rostów-Sewastopol
    collection.append(Connection(getCities()[30], getCities()[34]).createRoads([(1135, 483, 10), (1098, 468, 40), (1076, 435, 75), (1069, 398, 85)]))
    # 29 Rostów-Charków
    collection.append(Connection(getCities()[10], getCities()[30], color=COLORS.GRE).createRoads([(1106, 534, -30), (1143, 510, -45)]))
    # 30 Charków-Moskwa
    collection.append(Connection(getCities()[10], getCities()[26]).createRoads([(1071, 575, -72), (1057, 614, -72), (1039, 650, -55), (1011, 678, -35)]))
    # 31 Charków-Kijów
    collection.append(Connection(getCities()[10], getCities()[19]).createRoads([(1067, 525, 70), (1045, 494, 40), (1008, 490, -25), (975, 509, -35)]))
    # 32 Moskwa-Smoleńsk
    collection.append(Connection(getCities()[26], getCities()[35], color=COLORS.ORA).createRoads([(965, 707, -20), (939, 692, 85)]))
    # 33 Moskwa-Petersburg
    collection.append(Connection(getCities()[26], getCities()[29], color=COLORS.WHI).createRoads([(980, 722, -75), (959, 758, -55), (929, 790, -40), (890, 809, -15)]))
    # 34 Kijów-Smoleńsk
    collection.append(Connection(getCities()[19], getCities()[35], color=COLORS.RED).createRoads([(957, 553, 85), (956, 593, -80), (947, 634, -75)]))
    # 35 Kijów-Wilno
    collection.append(Connection(getCities()[19], getCities()[44]).createRoads([(930, 550, -40), (892, 581, -35), (852, 607, -30)]))
    # 36 Kijów-Warszawa
    collection.append(Connection(getCities()[19], getCities()[41]).createRoads([(917, 529, -10), (875, 531, 0), (832, 532, 0), (791, 535, -10)]))
    # 37 Kijów-Budapeszt
    collection.append(Connection(getCities()[7], getCities()[19], special=2).createRoads([(751, 408, 55), (782, 436, 35), (821, 455, 25), (860, 469, 20), (898, 483, 25), (932, 505, 45)]))
    # 38 Wilno-Smoleńsk
    collection.append(Connection(getCities()[35], getCities()[44], color=COLORS.YEL).createRoads([(914, 668, -15), (879, 659, 50), (847, 638, 30)]))
    # 39 Wilno-Warszawa
    collection.append(Connection(getCities()[41], getCities()[44], color=COLORS.RED).createRoads([(778, 567, 60), (808, 585, -10), (830, 600, -65)]))
    # 40 Wilno-Ryga
    collection.append(Connection(getCities()[31], getCities()[44], color=COLORS.GRE).createRoads([(778, 670, 80), (798, 640, -30)]))
    # 41 Wilno-Petersburg
    collection.append(Connection(getCities()[29], getCities()[44], color=COLORS.BLU).createRoads([(859, 784, 75), (848, 742, 75), (839, 700, 75), (830, 658, 75)]))
    # 42 Ryga-Petersburg
    collection.append(Connection(getCities()[29], getCities()[31]).createRoads([(838, 805, 20), (800, 792, 20), (771, 765, 75), (774, 726, -70)]))
    # 43 Sztokholm-Petersburg
    collection.append(Connection(getCities()[29], getCities()[39], special=2).createRoads([(845, 836, -45), (808, 852, 0), (769, 852, 0), (728, 845, 15), (696, 821, 55), (679, 784, 75)]))
    # 44 Izmir-Stambuł
    collection.append(Connection(getCities()[16], getCities()[38], special=2).createRoads([(979, 152, 70), (991, 194, 70)]))
    # 45 Izmir-Katania
    collection.append(Connection(getCities()[16], getCities()[18], roadType="train", special=2).createRoads([(694, 57, 0), (734, 58, 0), (773, 61, 5), (812, 65, 5), (850, 70, 10), (887, 74, 5), (923, 83, 30), (954, 106, 45)]))
    # 46 Izmir-Ateny
    collection.append(Connection(getCities()[2], getCities()[16], roadType="train").createRoads([(904, 118, 25), (944, 126, 0)]))
    # 47 Stambuł-Sofia
    collection.append(Connection(getCities()[37], getCities()[38], color=COLORS.BLU).createRoads([(893, 238, -30), (931, 221, -20), (972, 217, 20)]))
    # 48 Stambuł-Bukareszt
    collection.append(Connection(getCities()[8], getCities()[38], color=COLORS.YEL).createRoads([(930, 298, -45), (949, 265, -75), (976, 237, -30)]))
    # 49 Bukareszt-Sofia
    collection.append(Connection(getCities()[8], getCities()[37], special=2).createRoads([(910, 294, 90), (891, 262, 35)]))
    # 50 Bukareszt-Budapeszt
    collection.append(Connection(getCities()[7], getCities()[8], special=2).createRoads([(767, 378, -15), (806, 366, -20), (850, 355, -15), (889, 338, -40)]))
    # 51 Bukareszt-Kijów
    collection.append(Connection(getCities()[8], getCities()[19]).createRoads([(926, 348, 65), (944, 400, 80), (957, 446, 70), (959, 490, -80)]))
    # 52 Ryga-Gdańsk
    collection.append(Connection(getCities()[14], getCities()[31], color=COLORS.PUR).createRoads([(715, 622, 50), (734, 659, 65), (758, 688, 30)]))
    # 53 Sztokholm-Kopenhaga
    collection.append(Connection(getCities()[20], getCities()[39], roadType="double", color=COLORS.WHI, color2=COLORS.YEL).createRoads([(601, 660, 60), (630, 695, 45), (655, 731, 55)]))
    # 54 Kopenhaga-Hanower
    collection.append(Connection(getCities()[15], getCities()[20], roadType="train").createRoads([(534, 551, 80), (538, 592, 80), (559, 624, 30)]))
    # 55 Gdańsk-Berlin
    collection.append(Connection(getCities()[3], getCities()[14]).createRoads([(603, 551, 80), (611, 588, 70), (637, 616, 30), (674, 614, -30)]))
    # 56 Gdańsk-Warszawa
    collection.append(Connection(getCities()[14], getCities()[41]).createRoads([(722, 591, -30), (750, 566, -55)]))
    # 57 Warszawa-Berlin
    collection.append(Connection(getCities()[3], getCities()[41], roadType="double", color=COLORS.PIN, color2=COLORS.YEL).createRoads([(626, 518, -30), (666, 517, 30), (698, 540, 45), (737, 548, -16)]))
    # 58 Warszawa-Wiedeń
    collection.append(Connection(getCities()[41], getCities()[43], color=COLORS.BLU).createRoads([(757, 515, 75), (737, 482, 40), (709, 456, 45), (685, 425, 60)]))
    # 59 Wiedeń-Budapeszt
    collection.append(Connection(getCities()[7], getCities()[43], roadType="double", color=COLORS.WHI, color2=COLORS.RED).createRoads([(704, 391, -20)]))
    # 60 Budapeszt-Zagrzeb
    collection.append(Connection(getCities()[7], getCities()[45], color=COLORS.ORA).createRoads([(728, 360, 60), (700, 334, 30)]))
    # 61 Budapeszt-Sarajewo
    collection.append(Connection(getCities()[7], getCities()[33], color=COLORS.PIN).createRoads([(755, 364, -45), (764, 323, 75), (749, 286, 50)]))
    # 62 Sarajewo-Sofia
    collection.append(Connection(getCities()[33], getCities()[37], special=2).createRoads([(773, 257, -8), (827, 252, -5)]))
    # 63 Sofia-Ateny
    collection.append(Connection(getCities()[2], getCities()[37], color=COLORS.PIN).createRoads([(868, 132, -65), (860, 174, 90), (861, 219, 85)]))
    # 64 Sarajewo-Zagrzeb
    collection.append(Connection(getCities()[33], getCities()[45], color=COLORS.RED).createRoads([(708, 256, 15), (671, 264, -35), (666, 299, 75)]))
    # 65 Sarajewo-Ateny
    collection.append(Connection(getCities()[2], getCities()[33], color=COLORS.GRE).createRoads([(846, 126, -40), (808, 157, -45), (777, 194, -55), (749, 234, -55)]))
    # 66 Ateny-Brindisi
    collection.append(Connection(getCities()[2], getCities()[5], roadType="train").createRoads([(855, 93, 15), (816, 95, -20), (780, 111, -25), (750, 138, -50)]))
    # 67 Katania-Brindisi
    collection.append(Connection(getCities()[5], getCities()[18], roadType="train").createRoads([(709, 150, 25), (691, 117, -80), (682, 79, 60)]))
    # 68 Rzym-Brindisi
    collection.append(Connection(getCities()[5], getCities()[32], color=COLORS.WHI).createRoads([(690, 174, -20), (641, 188, -15)]))
    # 69 Rzym-Wenecja
    collection.append(Connection(getCities()[32], getCities()[42], color=COLORS.PUR).createRoads([(600, 229, -85), (596, 272, -85)]))
    # 70 Rzym-Marsylia
    collection.append(Connection(getCities()[24], getCities()[32], special=2).createRoads([(459, 254, 20), (502, 259, -5), (540, 242, -40), (577, 213, -40)]))
    # 71 Rzym-Katania
    collection.append(Connection(getCities()[18], getCities()[32], roadType="train").createRoads([(651, 77, -50), (655, 112, 60), (650, 145, -40), (620, 173, -45)]))
    # 72 Berlin-Frankfurt
    collection.append(Connection(getCities()[3], getCities()[13], roadType="double", color=COLORS.RED, color2=COLORS.PUR).createRoads([(596, 500, 80), (569, 478, 15), (534, 465, 35)]))
    # 73 Berlin-Wiedeń
    collection.append(Connection(getCities()[3], getCities()[43], color=COLORS.GRE).createRoads([(623, 500, -45), (649, 466, -60), (665, 426, -70)]))
    # 74 Hanower-Amsterdam
    collection.append(Connection(getCities()[0], getCities()[15], color=COLORS.YEL).createRoads([(453, 552, 60), (487, 571, 0), (520, 551, -60)]))
    # 75 Hanower-Frankfurt
    collection.append(Connection(getCities()[13], getCities()[15], color=COLORS.GRE).createRoads([(526, 477, 50), (544, 502, -70)]))
    # 76 Hanower-Berlin
    collection.append(Connection(getCities()[3], getCities()[15], color=COLORS.BLU).createRoads([(584, 547, -45), (555, 546, 45)]))
    # 77 Amsterdam-Frankfurt
    collection.append(Connection(getCities()[0], getCities()[13], color=COLORS.WHI).createRoads([(464, 513, -25), (493, 485, -55)]))
    # 78 Frankfurt-Bruksela
    collection.append(Connection(getCities()[6], getCities()[13], color=COLORS.BLU).createRoads([(447, 474, -17), (484, 461, -16)]))
    # 79 Frankfurt-Paryż
    collection.append(Connection(getCities()[13], getCities()[28], roadType="double", color=COLORS.WHI, color2=COLORS.ORA).createRoads([(413, 441, 20), (453, 441, -22), (490, 436, 35)]))
    # 80 Frankfurt-Monachium
    collection.append(Connection(getCities()[13], getCities()[25]).createRoads([(537, 447, -10), (562, 421, -80)]))
    # 81 Monachium-Zurych
    collection.append(Connection(getCities()[25], getCities()[46], color=COLORS.YEL, special=2).createRoads([(544, 405, -30), (515, 390, 75)]))
    # 82 Monachium-Wenecja
    collection.append(Connection(getCities()[25], getCities()[42], color=COLORS.BLU, special=2).createRoads([(600, 339, 75), (590, 376, -55)]))
    # 83 Monachium-Wiedeń
    collection.append(Connection(getCities()[25], getCities()[43], color=COLORS.ORA).createRoads([(588, 415, 50), (619, 435, 0), (652, 416, -45)]))
    # 84 Zagrzeb-Wiedeń
    collection.append(Connection(getCities()[43], getCities()[45]).createRoads([(653, 378, 60), (657, 344, -56)]))
    # 85 Zagrzeb-Wenecja
    collection.append(Connection(getCities()[42], getCities()[45]).createRoads([(616, 298, -20), (654, 304, 38)]))
    # 86 Zurych-Wenecja
    collection.append(Connection(getCities()[42], getCities()[46], color=COLORS.GRE, special=2).createRoads([(562, 318, -15), (529, 341, -55)]))
    # 87 Zurych-Marsylia
    collection.append(Connection(getCities()[24], getCities()[46], color=COLORS.PIN, special=2).createRoads([(459, 283, 60), (487, 327, 58)]))
    # 88 Paryż-Marsylia
    collection.append(Connection(getCities()[24], getCities()[28]).createRoads([(428, 274, -86), (421, 315, -76), (410, 357, -72), (396, 400, -75)]))
    # 89 Zurych-Paryż
    collection.append(Connection(getCities()[28], getCities()[46], special=2).createRoads([(407, 412, -39), (442, 390, -30), (481, 375, -20)]))


def getObjectives():
    objectives = [[(1, 2, 5), (7, 37, 5), (13, 20, 5), (12, 30, 5), (16, 37, 5), (5, 46, 6), (7, 46, 6), (35, 41, 6),
                   (5, 45, 6), (0, 27, 6), (19, 29, 7), (28, 45, 7), (4, 24, 7), (3, 22, 7), (11, 28, 7), (6, 40, 7),
                   (16, 32, 8), (33, 34, 8), (9, 23, 8), (28, 43, 8), (25, 40, 8), (4, 42, 8), (30, 35, 8), (15, 24, 8),
                   (19, 36, 8), (3, 8, 8), (23, 46, 9), (6, 14, 9), (3, 32, 9), (8, 31, 9), (22, 43, 9), (18, 38, 10),
                   (15, 19, 10), (38, 42, 10), (1, 10, 11), (39, 43, 11), (2, 44, 12), (3, 26, 12), (0, 44, 12), (13, 35, 13)],
                  [(14, 21, 20), (4, 29, 20), (2, 11, 20), (18, 26, 21), (12, 20, 21), (17, 39, 21)]]
    return objectives


def getGraph(connections, bot=None):
    graf = []
    cities = getCities()
    for i in range(47):
        polaczenia = []
        zrobione = False
        for j in connections:
            if j.claimedBy is not None:
                if j.claimedBy != bot:
                    continue
                if j.claimedBy == bot:
                    zrobione = True
            if j.cities[0].name == cities[i].name:
                nr = 0
                for k in range(len(cities)):
                    if cities[k].name == j.cities[1].name:
                        nr = k
                if zrobione:
                    polaczenia.append((nr, 0))
                else:
                    polaczenia.append((nr, j.roadLength))
            elif j.cities[1].name == cities[i].name:
                nr = 0
                for k in range(len(cities)):
                    if cities[k].name == j.cities[0].name:
                        nr = k
                if zrobione:
                    polaczenia.append((nr, 0))
                else:
                    polaczenia.append((nr, j.roadLength))
        graf.append(polaczenia)
    macin = 12  # TODO check and delete
    return graf


def countCards(cards, color):
    count = 0
    for i in cards:
        if i[0] == color:
            count = count + 1
    return count


class City:
    def __init__(self, name, location):
        self.name = name
        self.location = location


class Road:
    def __init__(self, center, angle, size=(36, 12), double_color=False, tunnel=False, train=False):
        self.win = None
        self.position = center
        self.size = size
        self.angle = angle
        self.type = double_color
        self.tunnel = tunnel
        self.train = train
        self.shapes = []
        px, py = self.position
        sx, sy = self.size
        if sx < sy:
            self.size = (sy, sx)
            sx, sy = self.size

        # Creating Road
        if not self.train:
            if self.tunnel:
                self.shapes.append(angledRectangle(self.position, self.size, self.angle))
                self.shapes[0].setFill(COLORS.GRA.value)
                self.size = (sx * 0.75, sy)
            if self.type:
                a, b = tempFunc(self.position, self.size, self.angle)
                self.shapes.append(a)
                self.shapes.append(b)
            else:
                self.shapes.append(angledRectangle(self.position, self.size, self.angle))
        else:
            self.shapes.append(angledRectangle(self.position, self.size, self.angle))
            self.shapes[0].setFill(COLORS.SIL.value)
            t = Circle(Point(px, py), sy * 0.375)
            t.setFill(COLORS.GRA.value)
            self.shapes.append(t)

    def addColor(self, color1, color2=None):
        if color2 is None:
            color2 = color1
        if not self.train:
            i = 0
            if self.tunnel:
                i = 1
            if self.type:
                self.shapes[i].setFill(color1)
                self.shapes[i + 1].setFill(color2)
            else:
                self.shapes[i].setFill(color1)
        return self

    def draw(self, win):
        self.win = win
        for s in self.shapes:
            s.draw(win)

    def undraw(self):
        for s in self.shapes:
            s.undraw()

    def conquer(self, player):
        sx, sy = self.size
        newblock = angledRectangle(self.position, (sx * 0.75, sy * 0.75), self.angle)
        newblock.setFill(player.color)
        self.shapes.append(newblock)
        if self.win is not None:
            newblock.draw(self.win)

    def requiresTrain(self):
        return self.train


class Connection:
    def __init__(self, city1, city2, roadType="single", color=COLORS.SIL, color2=None, special=1):
        self.roads = []
        self.cities = [city1, city2]
        self.roadType = roadType
        self.color = (color, color2)
        self.special = special
        self.roadLength = 0
        self.claimedBy = None

    def createRoads(self, blocks):
        self.roadLength = len(blocks)
        if self.roadType == "train":
            trains = self.special
            for i in range(self.roadLength):
                if trains > 0:
                    self.roads.append(Road((blocks[i][0], blocks[i][1]), blocks[i][2], train=True))
                    trains = trains - 1
                else:
                    self.roads.append(Road((blocks[i][0], blocks[i][1]), blocks[i][2]).addColor(COLORS.SIL.value))
        elif self.roadType == "double":
            if self.special != 1:
                for i in range(self.roadLength):
                    self.roads.append(
                        Road((blocks[i][0], blocks[i][1]), blocks[i][2], double_color=True, tunnel=True)
                        .addColor(self.color[0].value, self.color[1].value))
            else:
                for i in range(self.roadLength):
                    self.roads.append(Road((blocks[i][0], blocks[i][1]), blocks[i][2], double_color=True)
                                      .addColor(self.color[0].value, self.color[1].value))
        else:
            if self.special != 1:
                for i in range(self.roadLength):
                    self.roads.append(Road((blocks[i][0], blocks[i][1]), blocks[i][2], tunnel=True).addColor(self.color[0].value))
            else:
                for i in range(self.roadLength):
                    self.roads.append(Road((blocks[i][0], blocks[i][1]), blocks[i][2]).addColor(self.color[0].value))
        return self

    def draw(self, window):
        for r in self.roads:
            r.draw(window)

    def undraw(self):
        for r in self.roads:
            r.undraw()

    def checkForBuilding(self, player, color=None, extras=None):
        if extras is None:
            extras = []
        cards = []
        for i in player.cards:
            cards.append(i)
        if self.roadLength > player.wagons:
            return None
        if self.roadType == "train":
            if color is not None:
                if color != "silver" and color != "dimgrey":
                    trains = self.special
                    non_trains = self.roadLength - self.special
                    color_cards = 0
                    silver_cards = 0
                    for i in cards:
                        if non_trains > 0:
                            if i[0] == color:
                                color_cards = color_cards + 1
                                non_trains = non_trains - 1
                            elif i[0] == "silver":
                                silver_cards = silver_cards + 1
                                non_trains = non_trains - 1
                        elif trains > 0:
                            if i[0] == "silver":
                                silver_cards = silver_cards + 1
                                trains = trains - 1
                        else:
                            continue
                    if non_trains == 0 and trains == 0:
                        return color_cards, silver_cards
        elif self.roadType == "double":
            if self.special != 1:
                for i in extras:
                    cards.append(i)
            if color is not None:
                for j in 0, 1:
                    if color == self.color[j].value:
                        blocks = self.roadLength + countCards(extras, color)
                        color_cards = 0
                        silver_cards = 0
                        for i in cards:
                            if blocks > 0:
                                if i[0] == color:
                                    color_cards = color_cards + 1
                                    blocks = blocks - 1
                                elif i[0] == "silver":
                                    silver_cards = silver_cards + 1
                                    blocks = blocks - 1
                            else:
                                continue
                        if blocks == 0:
                            return color_cards, silver_cards
        elif self.roadType == "single":
            if self.special != 1:
                for i in extras:
                    cards.append(i)
            if color is not None:
                if color == player.targetConnection[1]:
                    blocks = self.roadLength + countCards(extras, color)
                    color_cards = 0
                    silver_cards = 0
                    for i in cards:
                        if blocks > 0:
                            if i[0] == color:
                                color_cards = color_cards + 1
                                blocks = blocks - 1
                            elif i[0] == "silver":
                                silver_cards = silver_cards + 1
                                blocks = blocks - 1
                        else:
                            continue
                    if blocks == 0:
                        return color_cards, silver_cards

        return None

    def buildConnection(self, player):
        player.claimedConnections.append(self)
        self.claimedBy = player
        for r in self.roads:
            r.conquer(player)


class Connections:
    def __init__(self):
        self.connections = []

    def makeConnections(self):
        createConnections(self.connections)

    def getConnection(self, city1, city2):
        for c in self.connections:
            if (c.cities[0].name == city1.name and c.cities[1].name == city2.name) or (
                    c.cities[0].name == city2.name and c.cities[1].name == city1.name):
                return c
        return None

    def draw(self, window):
        for c in self.connections:
            c.draw(window)
