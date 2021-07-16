# Arquivo contendo classes para a criação de objetos
# que compõem a hierarquia de classes
# Autor: Eduardo Augusto Rezaghi Taliani

##-------------------- Classes --------------------##
# Classe Pessoa
class Pessoa:
    # Método construtor da classe Pessoa
    def __init__(self, nome, fone):
        self.nome = nome
        self.fone = fone

    def exibir(self):
        print(f'-> {self.nome} - {self.fone}')

# Classe Squad
class Squad:
    # Método construtor da classe Squad
    def __init__(self,nome, techlead = None, devs = None):
        self.nome = nome
        self.devs = []
        self.techlead = techlead

    # Método auxiliar usando joined_lower case
    def incluir_techlead(self, techlead):
        self.techlead = techlead

    # Método auxiliar usando joined_lower case
    def incluir_dev(self, dev):
        self.devs.append(dev)

# Classe Colaborador (Pessoa -> Colaborador)
class Colaborador(Pessoa):
    # Método construtor da classe Colaborador
    def __init__(self,nome,fone, squad = None):
        super().__init__(nome,fone)
        self.squad = squad

    # Método auxiliar usando joined_lower case
    def incluir_squad(self, squad):
        self.squad = squad

# Classe Dev (Pessoa -> Colaborador -> Dev)
class Dev(Colaborador):
    # Método construtor da classe Dev
    def __init__(self,nome,fone,cargo, squad = None):
        super().__init__(nome,fone,squad)
        self.cargo = cargo

    def exibir(self):
        super().exibir()
        print(f'   Cargo de {self.cargo} na squad {self.squad.nome}\n')

##-------------------- Lógica de criação dos objetos --------------------##
print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Sky.One Solutions-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Bem vindo ao sistema de criação de squads!\n')

while True:
    squads = []

    nome_squad = input('\nNome da squad: ')
    squad = Squad(nome_squad)

    nome_techlead = input('Nome do techlead da squad: ')
    fone_techlead = input('Telefone do techlead: ')
    techlead = Colaborador(nome_techlead, fone_techlead)

    techlead.incluir_squad(squad)
    squad.incluir_techlead(techlead)

    squads.append(squad)

    while True:
        nome_dev = input('\nNome do desenvolvedor: ')
        fone_dev = input('Telefone do desenvolvedor: ')
        cargo_dev = input('Cargo do desenvolvedor: ')
        dev = Dev(nome_dev,fone_dev,cargo_dev)
        dev.incluir_squad(squad)

        squad.incluir_dev(dev)

        option = input('\n Deseja adicionar mais um dev? [S/N] ')
        if option in "Nn":
            break

    option = input('\n Deseja adicionar mais uma squad? [S/N] ')
    if option in "Nn":
        break

##-------------------- Exibição dos dados --------------------##
for squad in squads:
    print(f'\n------------------------------{squad.nome}------------------------------')
    print(f'TechLead: {squad.techlead.nome}')
    print('\n-------Desenvolvedores da squad-------')
    for dev in squad.devs:
        dev.exibir()
    print(f'\n------------------------------{squad.nome}------------------------------')
print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-Sky.One Solutions-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')