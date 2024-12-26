from Class import *
from tkinter import *
from windows_v2 import *
import csv

#Cores
cor1 = "#b1bae5" # lilás claro background color
cor2 = "#5469d1" # azul Vl
cor3 = "#3b3b3b" # preto
cor4 = "#feffff" # branco
cor5 = "#7d8ac7" # lilás esc. button

#Janela Adicionar Animal
def Animal():   
    #torna variaveis globais
    global screenAnimal
    global nr_animal_entry
    global name_entry
    global idade_entry
    global raca_entry
    global porte_entry
    global peso_entry
    global dono_entry
    global contato_entry
    global nif_entry
    global morada_entry

    screenAnimal =Tk()
    screenAnimal.title ("System Vet Py")
    screenAnimal.geometry ("800x720+600+200")
    screenAnimal.configure(bg=cor1)
    screenAnimal.resizable(False,False)

    # Adicionar imagens
    """ imagem = PhotoImage(file="D:\SystemVetPy\dog.png")
    label_imagem = Label(screenAnimal, image=imagem, bg='#b1bae5')
    label_imagem.pack()
    label_imagem.place(x=-40, y=520)

    imagem1 = PhotoImage(file="D:\SystemVetPy\patas.png")
    label_imagem1 = Label(screenAnimal, image=imagem1, bg='#b1bae5')
    label_imagem1.pack()
    label_imagem1.place(x=320, y=300) """

    #Criar Label
    label = Label(screenAnimal, text="Nº Chip: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=100)
    label = Label(screenAnimal, text="Nome: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=140)
    label = Label(screenAnimal, text="Idade: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=180)
    label = Label(screenAnimal, text="Raça: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=220)
    label = Label(screenAnimal, text="Porte: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=260)
    label = Label(screenAnimal, text="Peso: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=300)
    label = Label(screenAnimal, text="Dono: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=340)
    label = Label(screenAnimal, text="Tel.: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=380)
    label = Label(screenAnimal, text="Nif: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=460)
    label = Label(screenAnimal, text="Morada: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=540)

    #Adicionar TextBox
    nr_animal_entry=Entry(screenAnimal, width=30, font="Calibri 14")
    nr_animal_entry.pack(pady=10)
    nr_animal_entry.place(x=280, y=101)

    name_entry=Entry(screenAnimal, width=30, font="Calibri 14")
    name_entry.pack(pady=10)
    name_entry.place(x=280, y=141)

    idade_entry=Entry(screenAnimal, width=30, font="Calibri 14")
    idade_entry.pack(pady=10)
    idade_entry.place(x=280, y=181)

    raca_entry=Entry(screenAnimal, width=30, font="Calibri 14")
    raca_entry.pack(pady=10)
    raca_entry.place(x=280, y=221)

    porte_entry=Entry(screenAnimal, width=30, font="Calibri 14")
    porte_entry.pack(pady=10)
    porte_entry.place(x=280, y=261)

    peso_entry=Entry(screenAnimal, width=30, font="Calibri 14")
    peso_entry.pack(pady=10)
    peso_entry.place(x=280, y=301)

    dono_entry=Entry(screenAnimal, width=30, font="Calibri 14")
    dono_entry.pack(pady=10)
    dono_entry.place(x=280, y=341)

    contato_entry=Entry(screenAnimal, width=30, font="Calibri 14")
    contato_entry.pack(pady=10)
    contato_entry.place(x=280, y=381)

    nif_entry=Entry(screenAnimal, width=30, font="Calibri 14")
    nif_entry.pack(pady=10)
    nif_entry.place(x=280, y=421)

    morada_entry=Entry(screenAnimal, width=30, font="Calibri 14")
    morada_entry.pack(pady=10)
    morada_entry.place(x=280, y=461)

    # Adicionar botão
    button = Button(screenAnimal, text="Submeter", width=9, height= 1, font="Calibri 14", command=GuardarDados, bg=cor5, fg=cor3, relief="raised", overrelief="ridge")
    button.pack()
    button.place(x=483, y=580)
    button = Button(screenAnimal, text="Procurar", width=9, height= 1, font="Calibri 14", command=None, bg=cor5, fg=cor3, relief="raised", overrelief="ridge")
    button.pack()
    button.place(x=280, y=580)
    

    # Adicionar Titulos
    label = Label(screenAnimal, text="Vet Py", font="Calibri 32 bold",bg=cor1)
    label.place(x=290, y=0)
    label = Label(screenAnimal, text="Adicionar", font="Calibri 14 bold",bg=cor1)
    label.place(x=300, y=60)

    # Adicionar Menu lateral
    button = Button(screenAnimal, text="Consulta", font="Calibri 14",  bg=cor5, fg=cor3, width=10, command=Consulta, relief="raised", overrelief="ridge")
    button.pack()
    button.place(x=40, y=110)
    button = Button(screenAnimal, text="Animal", font="Calibri 14", bg=cor5, fg=cor3, width=10, command=Animal, relief="raised", overrelief="ridge")
    button.pack()
    button.place(x=40, y=180)
    button = Button(screenAnimal, text="Dono", font="Calibri 14", bg=cor5, fg=cor3, width=10, command=None, relief="raised", overrelief="ridge")
    button.pack()
    button.place(x=40, y=250)
    button = Button(screenAnimal, text="Gerir Dados", font="Calibri 14", bg=cor5, fg=cor3, width=10, command=Gerir_Dados, relief="raised", overrelief="ridge")
    button.pack()
    button.place(x=40, y=320)
    screenAnimal.mainloop()

def GuardarAnimal():
    #Inputs do Form Adicionar animal
    nr_animal= nr_animal_entry.get()
    nomeanimal= name_entry.get()
    idade= idade_entry.get()
    raca=raca_entry.get()
    porte=porte_entry.get()
    peso=peso_entry.get()
    dono=dono_entry.get()
    contato=contato_entry.get()
    nif=nif_entry.get()
    morada=morada_entry.get()

    #Cria uma lista onde armazena os dados intruduzidos pelo User
    listInputs=[nr_animal,nomeanimal,idade,raca,porte,peso,dono,contato,nif,morada]
    #listHeader=["Nr Chip","Nome","Idade","Raca","Porte","Peso","Dono","Contato","Nif","Morada"]
    
    #Adiciona a lista em cima no file exemplo.txt
    f = open('DadosAnimal.csv', 'a')
    writer = csv.writer(f)
    #writer.writerow(listHeader)
    writer.writerow(listInputs)
    f.close()

Animal()