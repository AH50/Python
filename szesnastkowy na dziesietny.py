#szesnastkowy na dziesietny
liczba=input()
i=len(liczba)
j=0
wynik=0
while i>0:
    if liczba[i-1]=="F":
        wynik=(((15)*(16**j))+wynik)
    elif liczba[i-1]=="E":
        wynik=(((14)*(16**j))+wynik)
    elif liczba[i-1]=="D":
        wynik=(((13)*(16**j))+wynik)
    elif liczba[i-1]=="C":
        wynik=(((12)*(16**j))+wynik)
    elif liczba[i-1]=="B":
        wynik=(((11)*(16**j))+wynik)
    elif liczba[i-1]=="A":
        wynik=(((10)*(16**j))+wynik)        
    else:
        wynik=(((int(liczba[i-1]))*(16**j))+wynik)
    
    
    j=j+1
    i=i-1
    
print(wynik)