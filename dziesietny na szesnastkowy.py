#dziesietny na szesnastkowy
liczba=int(input())
cyfry="0123456789ABCDEF"
wynik=""
while liczba>0:
    wynik=cyfry[liczba%16]+wynik
    print(wynik)
    liczba=int(liczba/16)
print(wynik)
