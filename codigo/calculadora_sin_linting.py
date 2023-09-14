def solicitar_valores() :
  a=input("Valor a: ")
  b=input("Valor b: ")
  return int(a),int(b)
def limpiar( ):
  return  0,0
def imprimir(a,b,operacion,resultado):
  print(a,operacion,b,"=",resultado)
def sumar(a,b):
  resultado = a + b
  imprimir(a,b,"+",resultado)
def restar(a,b):
  resultado=a-b
  imprimir(a,b,"+",resultado)
def multiplicar(a,b):
  resultado=a*b
  imprimir(a,b,"+",resultado)
def dividir(a,b):
  resultado=a/b
  imprimir(a,b,"+",resultado)
def menu (a,b):
  while  True:
    print("1) Limpiar valores") 
    print("2) Solicitar valores")  
    print("3) Sumar (",a,"+",b,")")
    print("4) Restar (",a,"-",b,")")
    print("5) Multiplicar (",a,"*",b,")")
    print("6) Dividir (",a,"/",b,")")
    print("7) Fin"  ) 
    opcion=int(input("Opcion (1-7): "))
    if 1<=opcion<=7:
     break
  return opcion
def  main():
  a,b=0,0
  while True:
    opcion=menu(a,b)
    if opcion==7:
     break
    elif opcion==1:
     a,b=limpiar()
    elif opcion==2:
     a,b=solicitar_valores()
    elif opcion==3:
     sumar(a,b)
    elif opcion==4:
     restar(a,b)
    elif opcion==5:
     multiplicar(a,b)
    elif opcion==6:
     dividir(a,b)
main()