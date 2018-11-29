#dowolny na dziesietny
print("Podaj liczbe: ")
liczba=input()
print("Podaj system: ")
system=int(input())
i=len(liczba)
j=0
wynik=0
while i>0:
    wynik=int(ord(liczba[i-1])-55)*system**j+wynik
    i=i-1
    j=j+1
    
print(wynik)