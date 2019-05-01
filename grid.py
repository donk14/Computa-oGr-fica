from tkinter import *
import numpy as np
from algoritmos import bresenham

pixel_width = 30
w = 600
h = 600

def create_grid(event=None):
   
    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    c.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(0, w, pixel_width):
        c.create_line([(i, 0), (i, h)], tag='grid_line')

    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, pixel_width):
        c.create_line([(0, i), (w, i)], tag='grid_line')

def draw_point(c,  matrix):
    array_pixel_width = np.array([pixel_width,pixel_width])
    
    for i in matrix:
        
        i = np.array(i)
        d = i * array_pixel_width
        i = d + array_pixel_width
        d = np.concatenate((d,i), axis=None)
        d = d + pixel_width
        c.create_rectangle(*d, fill="red", outline = 'blue')

def draw_grid_labels(c, num):
    '''
    Desenha os numeros de identificação do grid.
    '''
    #Desenha os numeros da horizontal
    for i in range(1,int(num)):
        p1 = (pixel_width/2)*(i)*2 + (pixel_width/2)
        p2 = (pixel_width/2)
        c.create_text( p1,p2, text=i-1,width=200)

    #Desenha os numeros da vertical
    for i in range(1,int(num)):
        p1 = (pixel_width/2)
        p2 = (pixel_width/2)*(i)*2 + (pixel_width/2)
        c.create_text( p1,p2, text=i-1,width=200)


def Bt_bresenham(c):
    
    x0,y0,x1,y1 = ed.get().split(',')
    print("x(",x0,',',y0,')',x1,y1)

    points = bresenham((0,3),(3,9))
    draw_point(c,points)

    

#Atribuindo a váriável 'janela' a classe chamada TK
janela = Tk()

#Alterar o título da Janela Principal
janela.title('Trabalho de Computação Gráfica')

#Alterar a cor de fundo da Janela Principal alterando o dicionário 'Janela'
janela['bg'] = "pink"

#width x height + left + top 
janela.geometry('800x600+400+100')

#Variável ed armazena 
ed = Entry(janela)
entrada = (ed.place(x=610, y=150))

c = Canvas(janela, height=h, width=w, bg='white')
c.pack(expand=False,side=LEFT)

c.bind('<Configure>', create_grid)

draw_grid_labels(c, w/pixel_width )

#matrix = [[ 0,0 ], [5,3],[6,3]]




# command guarda uma referência da função Bt_bresenham(), não chama a função, por isso não tem
# os parênteses
bt_bres = Button(janela, width=20, text='Bresenham', command = Bt_bresenham)
bt_bres.place(x=600,y=100)





janela.mainloop()
