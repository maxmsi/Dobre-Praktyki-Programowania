#2. Napisz funkcję, która sprawdzi, czy dana tablica dwuwymiarowa jest "magicznym kwadratem" (atrybuty i wartości zwracane należy odpowiednio zadeklarować).

 #   Kwadrat magiczny – tablica składająca się z n wierszy i n kolumn (n>2), w którą wpisano n^2 różnych liczb naturalnych w ten sposób, że suma liczb w każdym wierszu, w każdej kolumnie i w każdej przekątnej jest taka sama (tzw. suma magiczna).




def isMagicSquare(mat):
    #obliczanie sumy przekatnej
    s = 0
    N= len(mat)
    for i in range(0, N):
        s = s + mat[i][i]

        # Suma rzędów
    for i in range(0, N):
        rowSum = 0;
        for j in range(0, N):
            rowSum += mat[i][j]

        #sprawdzenie czy każdy rząd jest rowny wartosci przekątnej
        if (rowSum != s):
            return False

    #Suma kolumn
    for i in range(0, N):
        colSum = 0
        for j in range(0, N):
            colSum += mat[j][i]

            #Sprawdzenie czy każda kolumna jest równa przkątnej
        if (s != colSum):
            return False

    return True


# Testowa macierz prawidlowa
mat = [[2, 7, 6],
       [9, 5, 1],
       [4, 3, 8]]
#Testowa macierz nie prawidlowa
notMagic = [[2, 7, 6],
       [9, 9, 1],
       [4, 3, 8]]

if (isMagicSquare(mat)):
    print("Magic Square")
else:
    print("Not a magic Square")


if (isMagicSquare(notMagic)):
    print("Magic Square")
else:
    print("Not a magic Square")