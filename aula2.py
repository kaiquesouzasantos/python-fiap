# ==================== AULA 2 ==================== 

# ARRAY(VETOR):
#lista preenchida estaticamente
lista_estatica = ["xpto", True]

#lista preenchida dinamicamente
lista_dinamica = [input("Digite o usuário: "), bool(int(input("Está logado? ")))]

#lista vazia
lista_vazia=[]

# PRATICA 1:
equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
  equipamentos.append(input("Equipamento: "))
  valores.append(float(input("Valor: ")))
  seriais.append(int(input("Número Serial: ")))
  departamentos.append(input("Departamento: "))
  resposta = input("Digite "+resposta+" para continuar: ").upper()

for indice in range(0,len(equipamentos)):
  print("Equipamento..: ", (indice+1))
  print("Nome.........: ", equipamentos[indice])
  print("Valor........: ", valores[indice])
  print("Serial.......: ", seriais[indice])
  print("Departamento.: ", departamentos[indice])

# PRATICA 2:
busca=input("Digite o nome do equipamento que deseja buscar: ")
for indice in range(0,len(equipamentos)):
  if busca==equipamentos[indice]:
    print("Valor..: ", valores[indice])
    print("Serial.:", seriais[indice])

# PRATICA 3:
depreciacao=input("Digite o nome do equipamento que será depreciado: ")
for indice in range(0,len(equipamentos)):
  if depreciacao==equipamentos[indice]:
    print("Valor antigo: ", valores[indice])
    valores[indice] = valores[indice] * 0.9
    print("Novo valor: ", valores[indice])

# PRATICA 4:
serial=int(input("Digite o serial do equipamento que será excluido: "))
for indice in range(0, len(departamentos)):
  if seriais[indice]==serial:
    del departamentos[indice]
    del equipamentos[indice]
    del seriais[indice]
    del valores[indice]
    break

for indice in range(0,len(equipamentos)):
  print("Equipamento..: ", (indice+1))
  print("Nome.........: ", equipamentos[indice])
  print("Valor........: ", valores[indice])
  print("Serial.......: ", seriais[indice])
  print("Departamento.: ", departamentos[indice])

# PRATICA 5:
inventario=[]
resposta = "S"
while resposta == "S":
  equipamento=[input("Equipamento: "),
            float(input("Valor: ")),
            int(input("Número Serial: ")),
            input("Departamento: ")]
  inventario.append(equipamento)
  resposta = input("Digite "+resposta+" para continuar: ").upper()

for elemento in inventario:
  print("Nome.........: ", elemento[0])
  print("Valor........: ", elemento[1])
  print("Serial.......: ", elemento[2])
  print("Departamento.: ", elemento[3])

busca=input("Digite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
  if busca==elemento[0]:
    print("Valor..: ", elemento[1])
    print("Serial.:", elemento[2])

depreciacao=input("Digite o nome do equipamento que será depreciado: ")
for elemento in inventario:
  if depreciacao==elemento[0]:
    print("Valor antigo: ", elemento[1])
    elemento[1] = elemento[1] * 0.9
    print("Novo valor: ", elemento[1])

serial=int(input("Digite o serial do equipamento que será excluído: "))
for elemento in inventario:
  if elemento[2]==serial:
    inventario.remove(elemento)

for elemento in inventario:
  print("Nome.........: ", elemento[0])
  print("Valor........: ", elemento[1])
  print("Serial.......: ", elemento[2])
  print("Departamento.: ", elemento[3])

# ==================== FUNÇÃO NO ARRAY ==================== 
valores=[]
for elemento in inventario:
  valores.append(elemento[1])
if len(valores)>0:
  print("O equipamento mais caro custa: ", max(valores))
  print("O equipamento mais barato custa: ", min(valores))
  print("O total de equipamentos é de: ", sum(valores))

'''
MAX() = MAIOR
MIN() = MENOR
SUM() = SOMA DOS ELEMENTOS
'''

# PRATICA 1:
inventario=[]
resposta = "S"

#adicionar item no inventario
while resposta == "S":
  equipamento=[input("Equipamento: "),
            float(input("Valor: ")),
            int(input("Número Serial: ")),
            input("Departamento: ")]
  inventario.append(equipamento)
  resposta = input("Digite "+resposta+" para continuar: ").upper()

#exibir dados do inventário
for elemento in inventario:
  print("Nome.........: ", elemento[0])
  print("Valor........: ", elemento[1])
  print("Serial.......: ", elemento[2])
  print("Departamento.: ", elemento[3])

#localizar um item no inventario
busca=input("Digite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
  if busca==elemento[0]:
    print("Valor..: ", elemento[1])
    print("Serial.:", elemento[2])

#depreciar itens no inventario
depreciacao=input("Digite o nome do equipamento que será depreciado: ")
for elemento in inventario:
  if depreciacao==elemento[0]:
    print("Valor antigo: ", elemento[1])
    elemento[1] = elemento[1] * 0.9
    print("Novo valor: ", elemento[1])

#excluir um item do inventario
serial=int(input("Digite o serial do equipamento que será excluído: "))
for elemento in inventario:
  if elemento[2]==serial:
    inventario.remove(elemento)

#exibir dados do inventário
for elemento in inventario:
  print("Nome.........: ", elemento[0])
  print("Valor........: ", elemento[1])
  print("Serial.......: ", elemento[2])
  print("Departamento.: ", elemento[3])

#resumo de valores do inventário
valores=[]
for elemento in inventario:
  valores.append(elemento[1])
if len(valores)>0:
  print("O equipamento mais caro custa: ", max(valores))
  print("O equipamento mais barato custa: ", min(valores))
  print("O total de equipamentos é de: ", sum(valores))

# ==================== FUNÇÃO ==================== 
'''
def <identificador da funcao> (<parametro(s)>):
	<código que será executado>
	return <Dado que será retornado, caso seja necessário>
'''

# PRATICA 1:
def preencherInventario(lista):
  resp="S"
  while resp == "S":
    equipamento=[input("Equipamento: "),
              float(input("Valor: ")),
              int(input("Número Serial: ")),
              input("Departamento: ")]
    lista.append(equipamento)
    resp = input("Digite "+resp+" para continuar: ").upper()

# PRATICA 2:
def preencherInventario(lista):
  resp="S"
  while resp == "S":
    equipamento=[input("Equipamento: "),
              float(input("Valor: ")),
              int(input("Número Serial: ")),
              input("Departamento: ")]
    lista.append(equipamento)
    resp = input("Digite "+resp+" para continuar: ").upper()

def exibirInventario(lista):
  for elemento in lista:
    print("Nome.........: ", elemento[0])
    print("Valor........: ", elemento[1])
    print("Serial.......: ", elemento[2])
    print("Departamento.: ", elemento[3])

# PRATICA 3:
def localizarPorNome(lista):
  busca=input("Digite o nome do equipamento que deseja buscar: ")
  for elemento in lista:
    if busca==elemento[0]:
      print("Valor..: ", elemento[1])
      print("Serial.:", elemento[2])
    
# PRATICA 4:
def depreciarPorNome(lista, porc):
  depreciacao=input("Digite o nome do equipamento que será depreciado: ")
  for elemento in lista:
    if depreciacao==elemento[0]:
      print("Valor antigo: ", elemento[1])
      elemento[1] = elemento[1] * (1-porc/100)
      print("Novo valor: ", elemento[1])

# PRATICA 5:
def excluirPorSerial(lista):
  serial=int(input("Digite o serial do equipamento que será excluido: "))
  for elemento in lista:
    if elemento[2]==serial:
      lista.remove(elemento)
  return "Itens excluídos."

# PRATICA 6:
def resumirValores(lista):
  valores=[]
  for elemento in lista:
    valores.append(elemento[1])
  if len(valores)>0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ", min(valores))
    print("O total de equipamentos é de: ", sum(valores))