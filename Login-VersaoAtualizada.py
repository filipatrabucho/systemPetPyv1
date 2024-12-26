from tkinter import *
from tkinter import messagebox

#Cores
cor1 = "#b1bae5" # verde-água background color
cor2 = "#5469d1" # azul Vl
cor3 = "#3b3b3b" # preto
cor4 = "#feffff" # branco

def ValidateLogs():
    userid= usernametext.get()
    passwordid= passwordtext.get()
    if userid=="admin" and passwordid=="2559":
        messagebox.showinfo("Log in com Sucesso","Bem-vindo Admin") 
        ListaMenu()
        print("Lista de menus aberta")
        #login.withdraw()
    else:
        messagebox.showerror("Erro","Erro nos dados introduzidos")
def login():
    global username_input
    global password_input
    global usernametext
    global passwordtext
    global screen2
   
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
    Button(menu, text="Dono",width=10,height=1).pack()
    #Button(menu, text="Perfil",width=10,height=1).pack()
    
login()