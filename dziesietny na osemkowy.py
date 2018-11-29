#dziesietny na osemkowy
liczba=int(input())
wynik=""

while liczba>0:
    wynik=str(liczba%8)+wynik
    print(wynik)
    liczba=int(liczba/8)
print(wynik)