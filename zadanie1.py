def ile_krol(n,x,y):
    #konwersja stringu do int
    n = int(n)
    # -1 bo indeksowanie jest od 0 - czyli dla n = 8 od 0 do 7 a nie od 1 do 8
    index = n-1
    x = int(x) - 1
    y = int(y) - 1
    #tworzenie tablicy nxn i wypełnianie jej wartości 8
    tablica = []
    for i in range(n):
        tablica.append([])
        for j in range(n):
            tablica[i].append(8)
    #wypełnianie krawędzi bez wierzchołków
    for i in range(index):
        tablica[0][i+1] = 5
        tablica[index][i+1] = 5
        tablica[i+1][0] = 5
        tablica[i+1][index] = 5
    #wypełnianie wierzchołków
    tablica[0][0] = 3
    tablica[0][index] = 3
    tablica[index][0] = 3
    tablica[index][index] = 3

    #wyświetl wartość z pozycji króla
    print(tablica[x][y])



# Wczytywanie wartości
n, x, y = input("Podaj 3 wartości n ,x y po przecinku: ").split() 

#wywołanei funkcji
ile_krol(n,x,y)