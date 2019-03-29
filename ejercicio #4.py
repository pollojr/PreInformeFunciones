def hermano(num):
    n=num+1
    con=0
    for i in range(1,n+1):
        if n%i==0:
            con=con+1
    if con <=2 and num%6 != 0:
        print("el numero es primo hermano")
    else:
        print("el numero no es primo hermano")


num=int(input("ingrese un numero"))
hermano(num)
