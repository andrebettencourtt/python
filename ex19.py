contAlunos = 1      #inicializa a contagem de alunos
qtdAlunos = 6       #inserir nessa var a qtd de alunos
qtdNotas = 2        #inserir a qtd de notas

qtdAprovados = 0
qtdReprovados = 0 
qtdExame = 0
somaMedia = 0
mediaClasse = 0

while contAlunos <= qtdAlunos:
    print(f'Alunos {contAlunos}' )

    notaUm = int(input('Insira a primeira nota do aluno: '))
    notaDois = int(input('Insira a segunda nota do aluno: '))


    media = (notaUm + notaDois)/qtdNotas
    somaMedia += media

    if media < 3:
        print('Reprovado')
        qtdReprovados += 1
    elif media >= 3 and media < 7:
        print('Exame')
        qtdExame += 1
    elif media >= 7:
        print('Aprovado')
        qtdAprovados += 1



    contAlunos += 1      #contAlunos = contAlunos + 1


mediaClasse - somaMedia/qtdAlunos


print(f'Alunos aprovados {qtdAprovados}')
print(f'Alunos reprovados {qtdReprovados}')
print(f'Alunos exame {qtdExame}')