from tkinter import *
import math


#Atribuindo a váriável 'janela' a classe chamada TK
janela = Tk()

#Alterar o título da Janela Principal
janela.title('Trabalho de Computação Gráfica')

#Alterar a cor de fundo da Janela Principal alterando o dicionário 'Janela'
janela['bg'] = "pink"



#Definindo como o container a janela principal
lb = Label(janela, text='Olá Mundo!')

#Está contido no gerenciador de layout place
lb.place(x=370, y=300)

#Variável ed armazena 
ed = Entry(janela)
entrada = (ed.place(x=610, y=150))

def Bt_bresenham():
    
    x0,y0,x1,y1 = ed.get().split(',')
    print("x(",x0,',',y0,')',x1,y1)
    #ed.set('')


def Bt_curvaBesier():
    print('Curva de Besier')

def Bt_preenchimento():
    print('Preenchimento')

def Bt_recorte():
    print('Recorte')

def Bt_transformacao():
    print('Transformação')

# command guarda uma referência da função Bt_bresenham(), não chama a função, por isso não tem
# os parênteses
bt_bres = Button(janela, width=20, text='Bresenham', command = Bt_bresenham)
bt_bres.place(x=600,y=100)

bt_curva = Button(janela, width=20, text='Curva de Besier', command = Bt_curvaBesier)
bt_curva.place(x=600,y=200)

bt_preenchimento = Button(janela, width=20, text='Preenchimento', command = Bt_preenchimento)
bt_preenchimento.place(x=600,y=300)

bt_recorte = Button(janela, width=20, text='Recorte', command = Bt_recorte)
bt_recorte.place(x=600,y=400)

bt_transformacao = Button(janela, width=20, text='Transformação', command = Bt_transformacao)
bt_transformacao.place(x=600,y=500)

#width x height + left + top 
janela.geometry('800x600+400+100')

#Cria uma refência para nossa janela principal
janela.mainloop()
 
