from tkinter import *
from tkinter import Label, PhotoImage, messagebox
 
#Cores
cor1 = "#b1bae5" # lilás claro background color
cor2 = "#5469d1" # azul Vl (não usei)
cor3 = "#000000" # preto
cor4 = "#ffffff" # branco
cor5 = "#7d8ac7" # lilás esc. button

""" Criar Novo User """
""" def register_user():
    username_info=username.get()
    password_info=password.get()

    file=open("dados"+".txt","w")
    file.write(f"Username: {username_info}")
    file.write(f"Password: {password_info}")
    file.close()

    username_entry.delete(0,END)
    password_entry.delete(0,END)

    Label(screen1, text="Registo Efetuado com sucesso", fg="green", font=("calibri",11)).pack()

def register():
    global screen1 
    global username 
    global password
    global username_entry 
    global password_entry
    
    screen1=Toplevel(screen)
    screen1.title("Registar")
    screen1.geometry("500x500")
    screen1.configure(bg=cor1)
    username=StringVar()
    password=StringVar()

    Label(screen1,text="Preencha os dados",bg=cor1).pack()
    Label(screen1,text="",bg=cor1).pack()
    Label(screen1,text="Username:",bg=cor1).pack()
    username_entry=Entry(screen1,textvariable=username).pack()
    Label(screen1,text="Password:",bg=cor1).pack()
    password_entry=Entry(screen1,textvariable=password,show="*").pack()
    Label(screen1,text="",bg=cor1).pack()
    Button(screen1, text="Registar",width=10,height=1,command=register_user).pack()
 """


""" def main_screen():
    global screen
    screen=Tk()
    screen.geometry("500x500")
    screen.title("System Pet Py")
    screen.configure(bg=cor1)

    Label(text="",bg=cor1).pack()
    Button(text="Entrar",height="2",width="30",bg="#7d8ac7",font=("calibri",11),relief = RAISED, overrelief = RIDGE,command=login).pack()
    Label(text="",bg=cor1).pack()
    Button(text="Registar",height="2",width="30",fg="#fff",bg="#7d8ac7",font=("calibri",11),relief = RAISED, overrelief = RIDGE,command=register).pack()
    screen.mainloop() """

def Animal():   
    global screenAnimal
    #Criar Janela
    screenAnimal =Tk()
    screenAnimal.title ("System Vet Py")
    screenAnimal.geometry ("800x720+600+200")
    screenAnimal.configure(bg=cor1)
    screenAnimal.resizable(False,False)

    # Adicionar imagens
    imagem = PhotoImage(file="D:\SystemVetPy\dog.png")
    label_imagem = Label(screenAnimal, image=imagem, bg='#b1bae5')
    label_imagem.pack()
    label_imagem.place(x=-40, y=520)

    imagem1 = PhotoImage(file="D:\SystemVetPy\patas.png")
    label_imagem1 = Label(screenAnimal, image=imagem1, bg='#b1bae5')
    label_imagem1.pack()
    label_imagem1.place(x=320, y=300)

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
    label = Label(screenAnimal, text="Morada: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=380)
    label = Label(screenAnimal, text="Cód. Postal: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=420)
    label = Label(screenAnimal, text="Tel.: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=460)
    label = Label(screenAnimal, text="E-mail: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=500)
    label = Label(screenAnimal, text="NIF: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=540)

    #Adicionar TextBox
    text_box=Entry(screenAnimal, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=101)
    text_box=Entry(screenAnimal, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=141)
    text_box=Entry(screenAnimal, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=181)
    text_box=Entry(screenAnimal, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=221)
    text_box=Entry(screenAnimal, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=261)
    text_box=Entry(screenAnimal, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=301)
    text_box=Entry(screenAnimal, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=341)
    text_box=Entry(screenAnimal, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=381)
    text_box=Entry(screenAnimal, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=421)
    text_box=Entry(screenAnimal, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=461)
    text_box=Entry(screenAnimal, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=501)
    text_box=Entry(screenAnimal, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=541)

    # Adicionar botão
    button = Button(screenAnimal, text="Submeter", width=9, height= 1, font="Calibri 14", command=None, bg=cor5, fg=cor3, relief="raised", overrelief="ridge")
    button.pack()
    button.place(x=483, y=580)
    button = Button(screenAnimal, text="Procurar", width=9, height= 1, font="Calibri 14", command=Gerir_Dados, bg=cor5, fg=cor3, relief="raised", overrelief="ridge")
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

    #screenAnimal.mainloop()
#Animal()

def Gerir_Dados():
    global screenGerirDados
    #Criar Janela
    screenGerirDados =Tk()
    screenGerirDados.title ("System Vet Py")
    screenGerirDados.geometry ("800x720+600+200")
    screenGerirDados.configure(bg=cor1)
    screenGerirDados.resizable(False,False)

    # Adicionar imagens
    """ imagem = PhotoImage(file="D:\SystemVetPy\dog.png")
        label_imagem = Label(screenGerirDados, image=imagem, bg='#b1bae5')
        label_imagem.pack()
        label_imagem.place(x=-40, y=520)

        imagem1 = PhotoImage(file="D:\SystemVetPy\patas.png")
        label_imagem1 = Label(screenGerirDados, image=imagem1, bg='#b1bae5')
        label_imagem1.pack()
        label_imagem1.place(x=320, y=300)
    """
    #Criar Label
    label = Label(screenGerirDados, text="Nº Chip: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=100)
    label = Label(screenGerirDados, text="Nome: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=140)
    label = Label(screenGerirDados, text="Idade: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=180)
    label = Label(screenGerirDados, text="Raça: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=220)
    label = Label(screenGerirDados, text="Porte: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=260)
    label = Label(screenGerirDados, text="Peso: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=300)
    label = Label(screenGerirDados, text="Dono: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=340)
    label = Label(screenGerirDados, text="Morada: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=380)
    label = Label(screenGerirDados, text="Cód. Postal: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=420)
    label = Label(screenGerirDados, text="Tel.: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=460)
    label = Label(screenGerirDados, text="E-mail: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=500)
    label = Label(screenGerirDados, text="NIF: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=540)

    #Adicionar TextBox
    text_box=Entry(screenGerirDados, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=101)
    text_box=Entry(screenGerirDados, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=141)
    text_box=Entry(screenGerirDados, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=181)
    text_box=Entry(screenGerirDados, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=221)
    text_box=Entry(screenGerirDados, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=261)
    text_box=Entry(screenGerirDados, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=301)
    text_box=Entry(screenGerirDados, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=341)
    text_box=Entry(screenGerirDados, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=381)
    text_box=Entry(screenGerirDados, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=421)
    text_box=Entry(screenGerirDados, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=461)
    text_box=Entry(screenGerirDados, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=501)
    text_box=Entry(screenGerirDados, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=541)

    # Adicionar botão
    button = Button(screenGerirDados, text="Apagar", width=9, height= 1, font="Calibri 14", command=None, bg=cor5, fg=cor3, relief="raised", overrelief="ridge")
    button.pack()
    button.place(x=484, y=580)
    button = Button(screenGerirDados, text="Procurar", width=9, height= 1, font="Calibri 14", command=None, bg=cor5, fg=cor3, relief="raised", overrelief="ridge")
    button.pack()
    button.place(x=280, y=580)
    button = Button(screenGerirDados, text="Editar", width=9, height= 1, font="Calibri 14", command=None, bg=cor5, fg=cor3, relief="raised", overrelief="ridge")
    button.pack()
    button.place(x=382, y=580)
    

    # Adicionar Titulos
    label = Label(screenGerirDados, text="Vet Py", font="Calibri 32 bold",bg=cor1)
    label.place(x=290, y=0)
    label = Label(screenGerirDados, text="Gerir Dados", font="Calibri 14 bold",bg=cor1)
    label.place(x=300, y=60)

    # Adicionar Menu lateral
    button = Button(screenGerirDados, text="Consulta", font="Calibri 14",  bg=cor5, fg=cor3, width=10, command=Consulta, relief="raised", overrelief="ridge")
    button.pack()
    button.place(x=40, y=110)
    button = Button(screenGerirDados, text="Animal", font="Calibri 14", bg=cor5, fg=cor3, width=10, command=Animal, relief="raised", overrelief="ridge")
    button.pack()
    button.place(x=40, y=180)
    button = Button(screenGerirDados, text="Dono", font="Calibri 14", bg=cor5, fg=cor3, width=10, command=None, relief="raised", overrelief="ridge")
    button.pack()
    button.place(x=40, y=250)
    button = Button(screenGerirDados, text="Gerir Dados", font="Calibri 14", bg=cor5, fg=cor3, width=10, command=Gerir_Dados, relief="raised", overrelief="ridge")
    button.pack()
    button.place(x=40, y=320)

    #screenGerirDados.mainloop()
#Gerir_Dados()

def Consulta():
    global screenConsulta
    #Criar Janela
    screenConsulta =Tk()
    screenConsulta.title ("System Vet Py")
    screenConsulta.geometry ("800x720+600+200")
    screenConsulta.configure(bg=cor1)
    screenConsulta.resizable(False,False)

    # Adicionar imagens
    imagem = PhotoImage(file="D:\SystemVetPy\dog.png")
    label_imagem = Label(screenConsulta, image=imagem, bg='#b1bae5')
    label_imagem.pack()
    label_imagem.place(x=-40, y=520)

    imagem1 = PhotoImage(file="D:\SystemVetPy\patas.png")
    label_imagem1 = Label(screenConsulta, image=imagem1, bg='#b1bae5')
    label_imagem1.pack()
    label_imagem1.place(x=320, y=300)

    #Criar Label
    label = Label(screenConsulta, text="Nº Chip: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=100)
    label = Label(screenConsulta, text="Nome: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=140)
    label = Label(screenConsulta, text="Idade: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=180)
    label = Label(screenConsulta, text="Raça: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=220)
    label = Label(screenConsulta, text="Porte: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=260)
    label = Label(screenConsulta, text="Peso: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=300)
    label = Label(screenConsulta, text="Dono: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=340)
    label = Label(screenConsulta, text="Data: ", font="Calibri 14",bg=cor1)
    label.place(x=190, y=380)
    
    #Adicionar TextBox
    text_box=Entry(screenConsulta, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=101)
    text_box=Entry(screenConsulta, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=141)
    text_box=Entry(screenConsulta, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=181)
    text_box=Entry(screenConsulta, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=221)
    text_box=Entry(screenConsulta, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=261)
    text_box=Entry(screenConsulta, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=301)
    text_box=Entry(screenConsulta, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=341)
    text_box=Entry(screenConsulta, width=30, font="Calibri 14")
    text_box.pack(pady=10)
    text_box.place(x=280, y=381)

    # Adicionar botão
    button = Button(screenConsulta, text="Procurar", width=9, height= 1, font="Calibri 14", command=None, bg=cor5, fg=cor3, relief="raised", overrelief="ridge")
    button.pack()
    button.place(x=484, y=580)
    button = Button(screenConsulta, text="Marcar", width=9, height= 1, font="Calibri 14", command=None, bg=cor5, fg=cor3, relief="raised", overrelief="ridge")
    button.pack()
    button.place(x=280, y=580)
    button = Button(screenConsulta, text="Desmarcar", width=9, height= 1, font="Calibri 14", command=None, bg=cor5, fg=cor3, relief="raised", overrelief="ridge")
    button.pack()
    button.place(x=382, y=580)
    

    # Adicionar Titulos
    label = Label(screenConsulta, text="Vet Py", font="Calibri 32 bold",bg=cor1)
    label.place(x=290, y=0)
    label = Label(screenConsulta, text="Consultas", font="Calibri 14 bold",bg=cor1)
    label.place(x=300, y=60)

    # Adicionar Menu lateral
    button = Button(screenConsulta, text="Consulta", font="Calibri 14",  bg=cor5, fg=cor3, width=10, command=Consulta, relief="raised", overrelief="ridge")
    button.pack()
    button.place(x=40, y=110)
    button = Button(screenConsulta, text="Animal", font="Calibri 14", bg=cor5, fg=cor3, width=10, command=Animal, relief="raised", overrelief="ridge")
    button.pack()
    button.place(x=40, y=180)
    button = Button(screenConsulta, text="Dono", font="Calibri 14", bg=cor5, fg=cor3, width=10, command=None, relief="raised", overrelief="ridge")
    button.pack()
    button.place(x=40, y=250)
    button = Button(screenConsulta, text="Gerir Dados", font="Calibri 14", bg=cor5, fg=cor3, width=10, command=Gerir_Dados, relief="raised", overrelief="ridge")
    button.pack()
    button.place(x=40, y=320)

    #screenConsulta.mainloop()
#Consulta()
    
#Verifica que o Username= Admin e a Pass=2559
def ValidateLogs():
    userid= usernametext.get()
    passwordid= passwordtext.get()
    if userid=="admin" and passwordid=="2559":
        messagebox.showinfo("Log in com Sucesso","Bem-vindo Admin") 
        ListaMenu()
        print("Lista de menus aberta")
        login.withdraw()
    else:
        messagebox.showerror("Erro","Erro nos dados introduzidos")
def login():
    global username_input
    global password_input
    global usernametext
    global passwordtext
    global screen2
    #print("Login session started")
    #screen2=Toplevel(screen)
    screen2=Tk()
    screen2.title("Entrar")
    screen2.geometry("500x500")
    screen2.configure(bg=cor1)

    usernametext=StringVar()
    passwordtext=StringVar()
    Label(screen2,text="Log in",bg=cor1).pack()
    Label(screen2,text="",bg=cor1).pack()
    Label(screen2,text="Username:",bg=cor1).pack()
    username_input=Entry(screen2,textvariable=usernametext).pack()
    Label(screen2,text="Password:",bg=cor1).pack()
    password_input=Entry(screen2,textvariable=passwordtext,show="*").pack()
    Label(screen2,text="",bg=cor1).pack()
    Button(screen2, text="Registar",width=10,height=1,command=ValidateLogs).pack()
    screen2.mainloop()

def ListaMenu():
    global menu
    menu=Tk()
    menu.title("Menu")
    menu.geometry("500x500")
    menu.configure(bg=cor1)
    Button(menu, text="Consulta",width=10,height=1).pack()
    Button(menu, text="Animal",width=10,height=1).pack()
    Button(menu, text="Dono",width=10,height=1,command=login).pack()
    Button(menu, text="Registar",width=10,height=1,command=Gerir_Dados).pack()
    #Button(menu, text="Perfil",width=10,height=1).pack()
    
login()