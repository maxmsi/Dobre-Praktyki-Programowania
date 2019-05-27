import numpy as np


"""
Napisz funkcję, która sprawdzi, czy na szachownicy do gry w warcaby nie ma możliwości zbicia jakiegoś piona przez któregoś z graczy.

Funkcja powinna pobierać jako atrybuty szachownicę i identyfikator gracza (by było wiadomo, na rzecz którego z graczy poszukiwane jest bicie) oraz zwracać informację o położeniu pionu bądź pionów, które mają możliwość zbicia.
Należy wybrać odpowiednią reprezentację szachownicy (zalecana tablica dwuwymiarowa z odpowiednimi wartościami) oraz odpowiednią reprezentację informacji o położeniu pionu.

"""


def czy_można_zbić(matrix, player):
    matrix = np.array(matrix)

    if not sprawdzenie_planszy(matrix):
        return False

    pozycja= []

    if player == 1:
        other_player = 2
    else:
        other_player = 1
        player = 2

    for i, line in enumerate(matrix):
        for j, value in enumerate(line):
            if value == player:
                if (i-2 >= 0 and j + 2 < matrix.shape[0] and matrix[i - 1][j + 1] == other_player and matrix[i - 2][j + 2] == 0) \
                        or (i-2 >= 0 and j - 2 >= 0 and matrix[i - 1][j - 1] == other_player and matrix[i - 2][j - 2] == 0) \
                        or (i+2 < matrix.shape[0] and j + 2 < matrix.shape[0] and matrix[i + 1][j + 1] == other_player and matrix[i + 2][j + 2] == 0) \
                        or (i+2 < matrix.shape[0] and j - 2 >= 0 and matrix[i + 1][j - 1] == other_player and matrix[i + 2][j - 2] == 0):

                    pozycja.append((i, j))
    return pozycja


def sprawdzenie_planszy(matrix):
    """
    :param matrix: matrix with 8 lines and 8 columns; values only 0, 1, 2;
            0 - bez pionka
            1 - Gracz A
            2 - Gracz B
    :return: plansza do gry jest poprawna
    """
    matrix = np.array(matrix)
    # sprawdzenie rozmiaru
    if matrix.shape[0] != matrix.shape[1] or matrix.shape[0] != 8:
        return False

    if not wartosci_ok(matrix):
        return False

    if not sprawdz_ustawienie_czarnych(matrix):
        return False
    else:
        return True


def wartosci_ok(matrix):
    value_set = {0, 1, 2}
    for i, line in enumerate(matrix):
        for j, value in enumerate(line):
            if value not in value_set:
                return False
    return True


def sprawdz_ustawienie_czarnych(matrix):
    for i, line in enumerate(matrix):
        for j, value in enumerate(line):
            if i % 2 == j % 2 and value != 0:
                print("\nNiepoprawne ustawienie pól koloru czarnego")
                return False
    return True


#matrix
checkers = [[1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0, 0]]

checkers2 = [[0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 2, 0],
            [0, 1, 0, 0, 0, 1, 0, 0],
            [2, 0, 2, 0, 2, 0, 2, 0],
            [0, 2, 0, 2, 0, 2, 0, 2],
            [2, 2, 2, 0, 2, 0, 2, 0]]

result = []
Gracz=2

result = czy_można_zbić(checkers2,Gracz)

if (result!= 0):
    print ('\nDla gracza numer:',Gracz," Dostępne ruchy znajdują się na polu:")
    print (result)
else:
    print("Nie moża wykonać ruchu zbijania graczem numer :",Gracz)






