# ==================== AULA 4 ==================== 
'''
open(“<caminhoDoArquivo><nomeDoArquivo>”, “w”) => indica que você está abrindo um arquivo para o modo de escrita (w => write).

open(“<caminhoDoArquivo><nomeDoArquivo>”, “r”) => com a letra “r” (read) no segundo parâmetro da função.

open(“<caminhoDoArquivo><nomeDoArquivo>”, “a”) => dessa forma,você poderá ler e escrever no arquivo especificado.

open(“<caminhoDoArquivo><nomeDoArquivo>”, “x”) => permite criar um novo arquivo em modo exclusivo (eXclusive), ou seja, uma vez que você criou/abriu o arquivo, ninguém mais poderá abri-lo. Caso você tente abrir um arquivo que já existe, será retornada uma falha.

open(“<caminhoDoArquivo><nomeDoArquivo>”, “t”) => o arquivo que for aberto com o parâmetro “t” (text) irá retornar para o Python o seu conteúdo como string.
'''

with open("teste.txt", "w") as arquivo:
    arquivo.write("Nunca foi tão fácil criar um arquivo.")

with open("teste.txt", "w") as arquivo:
    arquivo.write("Continuação do texto.")

with open("pagina.html", "w") as pagina:
    pagina.write("<body> <h1> Esta é um teste para página WEB </h1>")
    pagina.write("<br><h2> Abaixo seguem alguns nomes importantes para o projeto:  </h2>")
    pagina.write("<h3>")
    nome=""
    while nome!="SAIR":
        nome = input("Digite um nome ou SAIR: ").upper()
        if nome!="SAIR":
            pagina.write("<br>"+nome)
    pagina.write("</h3></body>")

with open("teste.txt", "r") as arquivo:
    conteudo=arquivo.read()
print("Tipo de dado da variável",type(conteudo))
print("Conteúdo do arquivo:",conteudo)

# PRATICA 1:
inventario={}
opcao=int(input("Digite: "'''

    <1> para registrar ativo
    <2> para persistir em arquivo
                
    <3> para exibir ativos armazenados: '''
))
while opcao>0 and opcao<4:
    if opcao==1:
        resp="S"
        while resp=="S":
            inventario[input("Digite o número patrimonial: ")]=[
            input("Digite a data da última atualização: "),
            input("Digite a descrição: "),
            input("Digite o departamento: ")]
            resp=input("Digite <S> para continuar.").upper()
    elif opcao==2:
        with open("inventario.csv", "a") as inv:
            for chave, valor in inventario.items():
                inv.write(chave + ";" + valor[0] + ";" + 
					valor[1] + ";" +valor[2]+"")
                print("Persistido com sucesso!")
    elif opcao==3:
        with open("inventario.csv", "r") as inv:
            print(inv.readlines())
        opcao=int(input("Digite: "'''

            <1> para registrar ativo
            <2> para persistir em arquivo
                        
            <3> para exibir ativos armazenados: '''
        ))

