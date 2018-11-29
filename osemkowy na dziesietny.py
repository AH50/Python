#osemkowy na dziesietny
liczba=input()
i=len(liczba)
print(i)
j=0
wynik=0
while i>0:
    wynik=(((int(liczba[i-1]))*(8**j))+wynik)
    
    j=j+1
    i=i-1
    
print(wynik)