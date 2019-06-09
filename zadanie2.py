def ile_skoczek(n,x,y):
    #konwersja stringu do int
    n = int(n)
    x = int(x) 
    y = int(y) 
    #Skoczek na środku planszy może wykonać 8 ruchów - 'tworzymy te ruchy jako zmienne"
    a = [
        [2,1],
        [2,-1],
        [-1,2],
        [1,2],
        [-2,1],
        [-2,-1],
        [-1,-2],
        [1,-2]
        ]
    
    #Sprawdzamy czy po takim ruchu skoczek ze swojej pozycji nie wyjdzie po za plansze - jeśli nie to zliczamy to jako możliwe pole
    pola_atakowane = 0
    for i in range(len(a)):
        if ( (x+a[i][0] > 0) and (x+a[i][0] < n+1) and (y+a[i][1]>0) and (y+a[i][1] < n+1) ):
            pola_atakowane+=1
    
    print(pola_atakowane)

# Wczytywanie wartości
n, x, y = input("Podaj 3 wartości n ,x y po spacji: ").split() 

#wywołanei funkcji
ile_skoczek(n,x,y)