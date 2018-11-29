def dowolny_na_dec(liczba,system1):
    wynik=0
    j=0
    i=len(liczba)
    while i>0:
        if(ord(liczba[i-1])>65):
            wynik=int(ord(liczba[i-1])-55)*(system1**j)+wynik
        else:
            wynik=int(liczba[i-1])*(system1**j)+wynik
        i=i-1
        j=j+1
    return(wynik)
   
def dec_na_dowolny(liczba,system):
   
    wynik=""
    a="0123456789ABCDEFGHIJKLMNOPRSTUWXYZ"
    while liczba>0:
        wynik=a[liczba%system]+wynik
        liczba=int(liczba/system)
    return(wynik)
 
print("Podaj liczbe: ")
liczba =input()
print("Podaj system liczbowy z ktorego przeliczas: ")
system1=int(input())
print("Podaj system liczbowy na który przeliczas: ")
system2=int(input())
 
liczba_dec=dowolny_na_dec(liczba,system1)
print(dec_na_dowolny(liczba_dec,system2))