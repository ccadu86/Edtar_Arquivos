"""nome_arquivo = "exemplo.txt"

arquivo = open(nome_arquivo, "r")

# # Lê o conteúdo do arquivo
conteudo = arquivo.read()

arquivo.close()

print(conteudo)
"""
# ###################################################################

"""nome_arquivo = "exemplo.txt"

arquivo = open(nome_arquivo, "w")

# # Escreve no arquivo
arquivo.write("Senai Jundiai - CFP 502.\n")

arquivo.close()"""


# ##################################################################

# nome_arquivo = "exemplo.txt"

# arquivo = open(nome_arquivo, "a")

# # # Anexa dados ao arquivo
# arquivo.write("Curso Dev. Sistemas.\n")

# arquivo.close()


######################################################################


Arquivo = "Teste.txt"

with open(Arquivo, "w") as arquivo:
    arquivo.write("Esta é a primeira linha.\n")
    arquivo.write("Esta é a segunda linha.\n")
    arquivo.write("Esta é a terceira linha.\n")

print("Valores foram salvos em", arquivo)

with open(Arquivo, "r") as arquivo2:
    linhas = arquivo2.readlines()

print(linhas)

for linha in linhas:
    print(linha.strip())