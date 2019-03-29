def potencia(a,b):
    x=a**b
    print(x)
    return x


for i in range(0,2):
    a=int(input("ingrese la base"))
    b=int(input("ingrse el exponente"))
    if i ==0:
        valor_uno=potencia(a, b)
    else:
        valor_dos=potencia(a, b)

if valor_uno > valor_dos:
    print ("la primera potencia que ingreso es mayor")
else:
    print("la segunda operacion que ingreso es mayor")
