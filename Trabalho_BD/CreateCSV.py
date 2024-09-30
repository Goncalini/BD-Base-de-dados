import csv

# Dados a serem escritos no arquivo CSV
dados = [
    ['Reserva_Livro_id','Livro_id'],
    ['1','2'],
    ['2','1'],
    ['3','7'],
    ['4','3'],
    ['5','6']
]
# Caminho do arquivo CSV a ser criado
caminho_arquivo = 'C:/Users/Pc/OneDrive/Ambiente de Trabalho/BASESDADOS/ReservaLivro_Livro.csv'

# Escrever dados no arquivo CSV
with open(caminho_arquivo, 'w', newline='') as arquivo_csv:
    escritor = csv.writer(arquivo_csv, delimiter=',')
    escritor.writerows(dados)

print("Arquivo CSV criado com sucesso!")
