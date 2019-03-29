def primo(n):
    con=0
    for i in range(1,n+1):
        if n%i==0:
            con=con+1
        
    if con <=2:
        print("numero primo")
    else:
        print("numero no es primo")


n=int(input("ingrese numero a estudio"))
primo(n)
