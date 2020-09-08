from tkinter import *

raiz = Tk()

miFrame = Frame(raiz)
miFrame.pack()
reset_pantalla=False
operacion = ""
resultado = 0
num1 = 0
contadorR = 0
contadorM = 0
contadorD = 0

#-------------------------------pantalla
numeroPantalla=StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")
#-------------------------------cierre pantalla

#--------------------------------Teclado Pulsado
def numeroPulsado(numero):
    global operacion
    global reset_pantalla
    if reset_pantalla!=False:
        numeroPantalla.set(numero)
        reset_pantalla=False
    else:
        numeroPantalla.set(numeroPantalla.get() + numero)
#-----------------Suma
def suma(num):
    global operacion
    global resultado
    global reset_pantalla
    resultado+=int(num)
    operacion = "suma"
    reset_pantalla=True
    numeroPantalla.set(resultado)   
#-----------------Suma
#-----------------Resta
def resta(num):
    global operacion
    global resultado
    global num1
    global contadorR
    global reset_pantalla

    if (contadorR == 0):
        num1 = int(num)
        resultado = num1
    else:
        if (contadorR==1):
            resultado = num1-int(num)
        else:
            resultado = int(resultado) - int(num)
        
        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    operacion = "resta"

    reset_pantalla = True

    contadorR = contadorR + 1
#-----------------Resta
#-----------------Multiplicacion
def multiplicar(num):
    global operacion
    global resultado
    global num1
    global contadorM
    global reset_pantalla

    if (contadorM == 0):
        num1 = int(num)
        resultado = num1
    else:
        if (contadorM==1):
            resultado = num1*int(num)
        else:
            resultado = int(resultado) * int(num)
        
        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    operacion = "multiplicar"
    reset_pantalla = True
    contadorM = contadorM + 1
#-----------------Multiplicacion
#-----------------Division
def dividir(num):
    global operacion
    global resultado
    global num1
    global contadorD
    global reset_pantalla

    if (contadorD == 0):
        num1 = int(num)
        resultado = num1
    else:
        if (contadorD==1):
            resultado = num1/int(num)
        else:
            resultado = int(resultado) / int(num)
        
        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    operacion = "dividir"
    print(operacion)
    reset_pantalla = True
    contadorD = contadorD + 1
#-----------------Division

#-----------------Funcion el_resultado
def el_resultado():
    global resultado
    global operacion
    global contadorR
    global contadorM
    global contadorD
    #--------------------No servia porque la variable resultado estaba definida fuera de la estructura if, por eso al dar igual no imprimia el resultado
    if operacion=="suma":
        numeroPantalla.set(resultado+int(numeroPantalla.get()))
        resultado=0
    elif operacion=="resta":
        numeroPantalla.set(int(resultado)-int(numeroPantalla.get()))
        resultado=0
        contadorR=0
    elif operacion=="multiplicar":
        numeroPantalla.set(int(resultado)*int(numeroPantalla.get()))
        resultado=0
        contadorM=0
    elif operacion=="dividir":
        numeroPantalla.set(int(resultado)/int(numeroPantalla.get()))
        resultado=0
        contadorD=0
#-----------------Funcion el_resultado
#-----------------FUNCION BORRAR
def borrar():
    numeroPantalla.set("")
    operacion = ""
#-----------------FUNCION BORRAR

#--------------------------------Teclado Pulsado

#-------------------------------fila1
botonC=Button(miFrame, text="C", width=10, command=lambda:borrar())
botonC.grid(row=2, column=1, columnspan=5)
#-------------------------------fila1
#-------------------------------fila2
boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=3, column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=3, column=2)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=3, column=3)
botonDividir=Button(miFrame, text="/", width=3, command=lambda:dividir(numeroPantalla.get()))
botonDividir.grid(row=3, column=4)
#-------------------------------fila2
#-------------------------------fila3
boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=4, column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=4, column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=4, column=3)
botonMultiplicar=Button(miFrame, text="*", width=3, command=lambda:multiplicar(numeroPantalla.get()))
botonMultiplicar.grid(row=4, column=4)
#-------------------------------fila3
#-------------------------------fila4
boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=5, column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=5, column=2)
boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=5, column=3)
botonRestar=Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonRestar.grid(row=5, column=4)
#-------------------------------fila4
#-------------------------------fila5
boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=6, column=1)
botonComa=Button(miFrame, text=",", width=3, command=lambda:numeroPulsado(","))
botonComa.grid(row=6, column=2)
botonIgual=Button(miFrame, text="=", width=3, command=lambda:el_resultado())
botonIgual.grid(row=6, column=3)
botonSuma=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()))
botonSuma.grid(row=6, column=4)

#-------------------------------fila5


raiz.mainloop()