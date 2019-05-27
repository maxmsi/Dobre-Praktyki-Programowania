# 4. Napisz funkcję, która wypisze na ekranie zawartość tablicy dwuwymiarowej, przechodząc po jej elementach spiralnie

#    funkcja powinna pobierać jako atrybuty: tablicę (przydać się może wysokość i szerokość tablicy)
#    wypisywanie elementów powinno odbywać się jak w przykładzie:

#  1  2  3  4  5
#  16 17 18 19  6
#  15 24 25 20  7
#  14 23 22 21  8
#  13 12 11 10  9


def wyswietlSpiralnie(rzad, kolumny, a):


    k = 0;
    l = 0

    ''' k - pierwszy rzad indeks
        m - indeks ostatniego rzedu
        l - indkeds pierwszej kolumny
        n - indeks ostatniej kolumny
        i - iterator '''

    while (k < rzad and l < kolumny):

     #Pierwszy rząd

        for i in range(l, kolumny):
            print(a[k][i], end=" ")

        k += 1

     #Ostatnia kolumna


        for i in range(k, rzad):
            print(a[i][kolumny - 1], end=" ")

        kolumny -= 1

     #ostatni wiersz z pozostalych
        if (k < rzad):

            for i in range(kolumny - 1, (l - 1), -1):
                print(a[rzad - 1][i], end=" ")

            rzad -= 1

       #pierwsza kolumna z pozostalych
        if (l < kolumny):
            for i in range(rzad - 1, k - 1, -1):
                print(a[i][l], end=" ")

            l += 1

a =  [[1, 2, 3, 4, 5],
     [16, 17, 18, 19, 6],
     [15, 24, 25, 20, 7],
     [14, 23, 22, 21, 8],
     [13, 12, 11, 10, 9]]

R = 5;
C = 5;
wyswietlSpiralnie(R, C, a)

