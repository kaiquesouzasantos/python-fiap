# ==================== AULA 3 ==================== 

# DICIONARIO:
usuarios={}
usuarios={
    "Chaves":["Chaves Silva","17/06/1975","Recep_01"],
    "Quico":["Enrico Flores","03/06/1976","Raiox_02"],
    "Quico":["Enrico Flores","03/06/1976","Raiox_03"]
    }
usuarios["Florinda"]=["Florinda Flores", "26/11/2017", "Recep_01"]
usuarios["Florinda"]=["Florinda Flores", "26/11/2016", "Recep_01"]

print(usuarios)
print("##############========#########")
print("Dados: ",usuarios.get("Chaves"))

# PRATICA 1:
usuarios={}
opcao=input("O que deseja realizar?" +"<I> - Para Inserir um usuário"+"<P> - Para Pesquisar um usuário"+"<E> - Para Excluir um usuário"+"<L> - Para Listar um usuário: ").upper()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        chave=input("Digite o login: ").upper()
        nome=input("Digite o nome: ").upper()
        data=input("Digite a última data de acesso: ")
        estacao=input("Qual a última estação acessada: ").upper()
        usuarios[chave]=[nome, data, estacao]
    opcao = input("O que deseja realizar?" +"<I> - Para Inserir um usuário" +"<P> - Para Pesquisar um usuário" +"<E> - Para Excluir um usuário" +"<L> - Para Listar um usuário: ").upper()

chave=input("Digite o login: ").upper()
usuarios[chave]=[input("Digite o nome: ").upper(),
                 input("Digite a última data de acesso: "),
                 input("Qual a última estação acessada: ").upper()
]

usuarios[input("Digite o login: ").upper()]=[input("Digite o nome: ").upper(),
                 input("Digite a última data de acesso: "),
                 input("Qual a última estação acessada: ").upper()
]

# PRATICA 3:
def perguntar():
    resposta = input("O que deseja realizar?" +"<I> - Para Inserir um usuário" +"<P> - Para Pesquisar um usuário" +"<E> - Para Excluir um usuário" +"<L> - Para Listar um usuário: ").upper()
    return resposta

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                          input("Digite a última data de acesso: "),
                                          input("Qual a última estação acessada: ").upper()
    ]

def pesquisar(dicionario, chave):
    lista=dicionario.get(chave)
    if lista!=None:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estação.: " + lista[2])

def excluir(dicionario, chave):
    if dicionario.get(chave)!=None:
        del dicionario[chave]
    print("Objeto Eliminado")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("Login: ", chave)
        print("Dados: ", valor)

# TUPLA:
ips={}
resp="S"
while resp=="S":
    ips[(input("Digite os dois primeiros octetos: "),
       input("Digite os dois últimos octetos: "))]=input("Nome da máquina: ")
    resp=input("Digite <S> para continuar: ").upper()

print("Exibindo ip´s: ")
for ip in ips.keys():
    print(ip[0]+"."+ip[1])

print("Exibindo máquinas com o mesmo endereço: ")
pesquisa=input("Digite os dois últimos octetos: ")
for ip,nome in ips.items():
    print("Máquinas no mesmo endereço (redes diferentes)")
    if(ip[1]==pesquisa):
        print(nome)

print("Exibindo as máquinas que compõem uma mesma rede: ")
rede=input("Digite os dois primeiros octetos: ")
for ip,nome in ips.items():
    if(ip[0]==rede):
        print(nome)

# ENUMERATE:
usuarios={}
resp="S"
emails=[]
while resp=="S":
    emails.append(input("Digite um e-mail: ").lower())
    resp=input("Digite <S> para continuar: ").upper()

tupla = list(enumerate(emails))
for chave in range(0,len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]]=[input("Digite o nome"), input("Digite o nível")]

for chave,dado in usuarios.items():
    print("Usuario.:", chave[0])
    print("Email...: ",chave[1])
    print("Nome....: ", dado[0])
    print("Nível...: ", dado[1])