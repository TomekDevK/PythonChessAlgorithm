def czy_wieza(x,y,xk,yk):
    if( x == xk or y == yk):
        return True
    else:
        return False
def czy_goniec(x,y,xk,yk):
    if( abs(xk - x) == abs(yk -y) ):
        return True
    else:
        return False
def czy_hetman(x,y,xk,yk):
    if( czy_wieza(x,y,xk,yk) or czy_goniec(x,y,xk,yk)):
        return True
    else:
        return False
# Wczytywanie wartości
x, y, xk, yk = input("Podaj 4 wartości x, y, xk, yk po spacji: ").split() 
x = int(x)
y = int(y)
xk = int(xk)
yk = int(yk)
#wywołanei funkcji
print(czy_wieza(x,y,xk,yk))
print(czy_goniec(x,y,xk,yk))
print(czy_hetman(x,y,xk,yk))