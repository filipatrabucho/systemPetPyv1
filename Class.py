# class principal (método construtor), define os atributos iniciais do objeto Animal
class Animal():
    def __init__(self,nr_chip,nome, idade,raca,porte,peso,dono):
        self.nr_chip=nr_chip
        self.nome=nome
        self.idade=idade
        self.raca=raca
        self.porte=porte
        self.peso=peso 
        self.dono=dono
        self.nr_consulta=[] # Lista vazia para armazenar números de consulta
        self.excluido=False # flag para indicar se o animal foi excluído

    # Retorna o número do chip do animal
    def getNRChip(self):
        return self.nr_chip
       
    # Define informações do dono
    def Dono(self,contato,nif,morada):
        self.contato=contato
        self.nif=nif
        self.morada=morada  
    
    # Imprime na tela o número do chip e o nome do animal
    def RetornaDados(self):
        if not self.excluido:
            print(f"Nr Chip: {self.nr_chip} e Nome: {self.nome}")
        else:
            return "Animal excluído."
        
    # Mostra todas as informações do animal
    def MostrarInformacoes(self):
        if not self.excluido:
            print("\nDetalhes do Animal:")
            print(f"Nr Chip: {self.nr_chip}, Nome: {self.nome}, Idade: {self.idade}, Raça: {self.raca}, Porte: {self.porte}, Peso: {self.peso}, Dono: {self.dono}")
        else:
            return "Animal excluído."

    # Método para procurar um animal (recebe uma lista de animais e o nº do chip como parâmetro)
    def procurarAnimal(animais, nr_chip):
        for Animal in animais:                                     
            if Animal.nr_chip == nr_chip and not Animal.excluido:
                return Animal
        return None                                                

    # Método para permitir atualizar dados do animal
    def editarAnimal(self,nr_chip,nome,idade,raca,porte,peso,dono):
        if not self.excluido:
            self.nr_chip=nr_chip
            self.nome=nome
            self.idade=idade
            self.raca=raca
            self.porte=porte
            self.peso=peso 
            self.dono=dono
        else:
            return "Animal excluído."
    
    # Método para excluir os dados do animal-> configura a flag excluido para True
    def apagarAnimal(self):
        self.excluido = True
        print("Animal excluido com sucesso.")   

    # método para permitir que consultas sejam associadas a um animal
    def adicionarConsulta(self, consulta):
        if not self.excluido:
            self.nr_consulta.append(consulta)
        else:
            return "Animal excluído."

# Método construtor, define os atributos iniciais do objeto Consulta
class Consulta():
    def __init__(self,id,data,motivo,obs,bi):
        self.id=id
        self.data=data
        self.motivo=motivo
        self.obs=obs  
        self.bi=bi 
        self.excluido = False  # Flag para indicar se a consulta foi excluída
    
    # Imprime informações sobre a consulta      
    def historico(self):
        if not self.excluido:
            print(f"Nr Consultas: {self.id}, Data: {self.data}, Motivo: {self.motivo}, Obs: {self.obs}")
        else:
            return "Consulta excluída"  

    # Verifica se o nº do chip fornecido corresponde ao nº associado à consulta
    def VerificaChip(self, nr_chip):
        if not self.excluido:
            if(self.bi == nr_chip):
                nr_consulta=[self.id,self.data,self.motivo,self.obs,self.bi]
                print(f"A consulta: {nr_consulta}")
            else:
                print("Não existe consulta marcada para esse animal")
        else:
            return "Animal excluído"    
    
    # Método para procurar uma consulta (recebe uma lista de consulta e o nº do chip como parâmetro)
    def procurarConsulta(consultas, nr_chip):
        for Consulta in consultas:
            if Consulta.bi == nr_chip and not Consulta.excluido:
                return Consulta
        return None

    # Método para permitir atualizar dados da consulta
    def editarConsulta(self,id,data,motivo,obs,bi):
        self.id=id
        self.data=data
        self.motivo=motivo
        self.obs=obs  
        self.bi=bi 

    # Método para excluir os dados da consulta-> configura a flag excluido para True
    def apagarConsulta(self):
        self.excluido = True
        print("Consulta excluida com sucesso.")  

def main():

    c1=Consulta("1","31-02-2000","vacinas","hsadilhwa",1)          # instância da classe Consulta
    c2=Consulta("2","30-02-2000","gastro","consulta",1)          # instância da classe Consulta
    a1=Animal(1,"Jacob",2,"Pastor Alemao","Grande",30,"Alberto")   # instância da classe animal
    #c1.VerificaChip(a1.getNRChip())    #Chama o método VerificaChip da instância de Consulta (c1) passando o número do chip do animal (a1.getNRChip())
   
    a1.adicionarConsulta(c1)
    a1.adicionarConsulta(c2)
    a1.RetornaDados()
    print("\nConsultas associadas: ")
    for consulta in a1.nr_consulta:
        consulta.historico()

    print("\n")
    # Exemplo utilização método editar animal  
    a2=Animal(2, "Bob", 3, "Labrador", "Grande", 30, "Manuel")
    a2.MostrarInformacoes() 
    a2.editarAnimal(2, "Bob", 5, "Labrador", "Grande", 32, "Manuel")
    a2.MostrarInformacoes()

    print("\n")
    # Exemplo utilização método apagar animal
    a2.apagarAnimal()
    print(a2.MostrarInformacoes())

if __name__=="__main__":
    main()
