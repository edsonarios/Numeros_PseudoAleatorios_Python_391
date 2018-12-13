from tkinter import *

root=Tk()

root.title("Numeros PseudoAleatorios - Inf 391")
#root.resizable(0,0)
#root.config(bg="black")

miframe=Frame(root, width=500, height=400)
miframe.pack()
#PARA UNA IMAGEN
#miImagen=PhotoImage(file="imagen.gif")
#Label(miframe, image=miImagen).place(x=100,y=0)
#--------------------------------------------------------
#HEADER
title=Label(miframe, text="NUMEROS PSEUDOALEATORIOS", fg="red", font=("Comic Sans MS",18))#.place(x=50,y=0)
#title.grid(row=0,column=1, sticky="e", padx=10,pady=10)
#title=Label(miframe, text="")
title.grid(row=0,columnspan=5, sticky=W+E, padx=10,pady=10)
title1=Label(miframe, text="")
title1.grid(row=1,column=5, sticky=W+E, padx=10,pady=10)
#/HEADER----------------------------------------------------------

#BODY--------------------------------------------------------------
title=Label(miframe, text="INGRESE LOS DATOS", fg="black", font=("Comic Sans MS",14))
title.grid(row=1,column=0,columnspan=3, sticky="w", padx=10,pady=10)


label1=Label(miframe, text="SEMILLA",fg="black")
label1.grid(row=2,column=0, sticky="e", padx=10,pady=10)

label2=Label(miframe, text="a", fg="black", font=("Comic Sans MS",14))
label2.grid(row=3,column=0, sticky="e", padx=10,pady=10)

label3=Label(miframe, text="M",fg="black")
label3.grid(row=4,column=0, sticky="e", padx=10,pady=10)

label4=Label(miframe, text="c",fg="black")
label4.grid(row=5,column=0, sticky="e", padx=10,pady=10)

input1T=StringVar()
input1=Entry(miframe, textvariable=input1T)
input1.grid(row=2,column=1, sticky="e", padx=10,pady=10)

input2T=StringVar()
input2=Entry(miframe, textvariable=input2T)
input2.grid(row=3,column=1, sticky="e", padx=10,pady=10)

input3T=StringVar()
input3=Entry(miframe, textvariable=input3T)
input3.grid(row=4,column=1, sticky="e", padx=10,pady=10)

input6T=StringVar()
input6=Entry(miframe, textvariable=input6T)
input6.grid(row=5,column=1, sticky="e", padx=10,pady=10)

#RESULTADO
label4=Label(miframe, text="RESULTADO",fg="black", font=("Comic Sans MS",14))
label4.grid(row=7,column=0, sticky="w", padx=10,pady=10)

label5=Label(miframe, text="PERIODO DEL GENERADOR : ")
label5.grid(row=8,column=0, sticky="W", padx=10,pady=10)

input4T=StringVar()
input4=Entry(miframe, textvariable=input4T)
input4.grid(row=8,column=1, sticky="w", padx=10,pady=10)

result=StringVar()
input5=Text(miframe, width=30, height=15)
input5.grid(row=9,column=0,columnspan=4, sticky=E + W, padx=10,pady=10)

scroll=Scrollbar(miframe, command=input5.yview)
scroll.grid(row=9,column=5, sticky="nsew", padx=10,pady=10)

input5.config(yscrollcommand=scroll.set)

#BOTON----------------------------------------------------------------
def funcion1():
    input5.delete(0.0,END)
    
    x=float(input1.get())
    sw=0
    i=1
    while True:
        n=x**2
        cant = int(len(str(n)))
        d=(cant-4)/2
        x=n%(10**(d+4))
        x=x/(10**d)
        m=x/10000.00
        print (m,"float")
        print (i,".- ",m)
        if m==sw:
            break
        else:
            if i==1:
                sw=m
            i=i+1
            n=x
            continue
    print ('periodo= ',i)

    input4T.set(i)
    input5.insert(END,"El periodo es "+str(i))
#------------------------------------------------------------------------------------------    

def funcion2():
    Xo=float(input1T.get())
    a=float(input2T.get())
    m=float(input3T.get())
    c=float(input6T.get())
    periodo=0
    i = 0
    res=""
    input5.delete(0.0,END)
    array1=[]
    array2=[]
    sw=0
    aux=0.0
    aux2=0.0
    while i < 500:
        op=(a*Xo+c)%m
        Xn1=op
        Num=Xn1/m

        res+=str(i) +"  "+str(Xo)+"   "+ str(op)+"   "+str(Xn1)+"   "+str(Num)+"\n"
        j=0
        ind=len(array1)
        while j < ind:
            if op==array1[j] and Num==array2[j]:
                print("El periodo es : "+str(i))
                periodo=i
                i=500
                break
            j+=1
        array1.insert(i,op)
        array2.insert(i,Num)
        i+=1
        Xo=Xn1
        
    
    input4T.set(periodo)
    input5.insert(END,res)
#------------------------------------------------------------------------------------------  

def funcion3():
    input5.delete(0.0,END)
    a=float(input2T.get())
    m=float(input3T.get())
    x=float(input1T.get())
    periodo=0
    sw=x
    i=1
    res=""
    while True:
        n=(a*x)%m
        x=n
        print (i,".- ",n)
        res+=str(i) +"        "+str(n)+"\n"
        if x==sw:
            break
        else:
            i=i+1
            continue
    print ('periodo= ',i)
    periodo=i
    input4T.set(periodo)
    input5.insert(END,res)
#------------------------------------------------------------------------------------------  

def funcion4():
    input5.delete(0.0,END)
    a=float(input2T.get())
    m=float(input3T.get())
    x=float(input1T.get())
    periodo=0
    sw=x
    i=1
    res=""
    while True:
        n=(a*x)%m
        x=n
        print (i,".- ",n)
        res+=str(i) +"        "+str(n)+"\n"
        if x==sw:
            break
        else:
            i=i+1
            continue
    print ('periodo= ',i)
    periodo=i
    input4T.set(periodo)
    input5.insert(END,res)
#------------------------------------------------------------------------------------------  


button1=Button(miframe, text="Metodo 1", command=funcion1)
button1.grid(row=6,column=0)

button2=Button(miframe, text="Metodo 2", command=funcion2)
button2.grid(row=6,column=1)

button3=Button(miframe, text="Metodo 3", command=funcion3)
button3.grid(row=6,column=2)

button4=Button(miframe, text="Metodo 4", command=funcion4)
button4.grid(row=6,column=3)



root.mainloop()

"""METODO 2
var Xo=4
var a=5
var m=8
var c=7      //PERIODO 8

var Xo= 15
var a=50
var m=100   // PERIODO 2
var c=16

var Xo=0
var a=7
var m=10000      //PERIODO 100
var c=501

var Xo=2.0
var a=6.0
var m=1000.0      //PERIODO 126
var c=8.0

METDO 3
Xo=17
a=3
m=100

METDO 4
Xo=7
a=5
m=64
"""

