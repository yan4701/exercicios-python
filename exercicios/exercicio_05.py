# Calcular a média final dadas as notas das 3 provas e produzir uma saída com a média e a situação
# do aluno de acordo com o seguinte critério: média >= 7, aprovado; média >=3 e média < 7,
# recuperação; média < 3, reprovado. Considerar também o número de faltas do aluno: se forem
# mais que sete faltas, o aluno estará automaticamente reprovado (o usuário deve fornecer o
# numero de faltas). Se o aluno se encontrar em recuperação, solicitar a nota da quarta prova e,
# após calcular a media final, informar se o aluno passou (media final >=5) ou não.

# função para validar a entrada das notas (0 a 10)
def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Erro: A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Erro: Digite um númeor válido.")
  # função para validar a entrada de faltas (não pode ser negativo)          
def ler_faltas():
    while True:
        try:
            faltas = int(input("Digite a quantidade de faltas: "))
            if faltas >= 0:
                return faltas
            else:
                print("Erro: O número de faltas não pode ser negativo.")
        except ValueError:
            print("Erro: Digite um número inteiro válido.")
            
# Solicita as notas e faltas do aluno
nota1 = ler_nota("Digite a nota da primeira prova: ")
nota2 = ler_nota("Digite a nota da segunda prova: ")
nota3 = ler_nota("Digite a nota da terceira prova: ")
faltas = ler_faltas()

# Cálculo da média do aluno
media = (nota1 + nota2 + nota3) / 3

# Verifica se o aluno excedeu o limite de faltas
if faltas > 7:
    print("Aluno reprovado por excesso de faltas.")
    exit()  # Encerra o programa, pois o aluno já foi reprovado

# Se a média for maior ou igual a 7, aluno aprovado
if media >= 7:
    print(f"Aluno aprovado com média {media:.2f}.")

# Se a média estiver entre 3 e 7, aluno está em recuperação
elif media >= 3 and media <= 7:
    print(f"Aluno em recuperação com média {media:.2f}.")
    
    # Solicita a nota da prova de recuperação
    nota4 = ler_nota("Digite a nota da prova de recuperação: ")
    # Cálculo da nova média final com peso adequado (três notas anteriores + recuperação)
    media_final = (media * 3 + nota4) / 4

    # Verifica se o aluno passou na recuperação
    if media_final >= 5:
        print(f"Aluno aprovado na recuperação com média final {media_final:.2f}.")
    else:
        print(f"Aluno reprovado na recuperação com média final {media_final:.2f}.")

# Se a média for menor que 3, aluno reprovado
else:
    print(f"Aluno reprovado com média {media:.2f}.")
    